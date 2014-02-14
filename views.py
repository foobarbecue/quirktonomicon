from django.shortcuts import render, render_to_response
from quirktonomicon.models import Ideation, VoteCount, Flag, HourData
from quirktonomicon.utils import dt2jsts
from quirktonomicon import stats
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
import json
from cacheops import cached
from django.core import serializers
from collections import Counter
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt

def votes_plot(req, idea_id):
    idea=Ideation.objects.get(idea_id=idea_id)
    vote_counts=VoteCount.objects.filter(idea_id=idea_id)
    votes=vote_counts.values_list('accessed_at','votes_count')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
    return render(req, 'votes_plot.html', {'plot_data':plot_data, 'idea':idea})


def votes_plot_json(req, idea_id):
    @cached(timeout=7200)
    def _votes_plot_json_cacheable(idea_id):
        idea=Ideation.objects.get(idea_id=idea_id)
        vote_counts=VoteCount.objects.filter(idea_id=idea_id)
        votes=vote_counts.values_list('accessed_at','votes_count')
        plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
        plot_data = '['+plot_data+']'
        return HttpResponse(plot_data,content_type="application/json")
    return _votes_plot_json_cacheable(idea_id)


def idea_json(req, idea_id):
    @cached(timeout=7200)
    def _idea_json_cacheable(idea_id):    
        idea_dict = serializers.serialize('json', Ideation.objects.filter(idea_id=idea_id))
        return HttpResponse(idea_dict,content_type="application/json")
    return _idea_json_cacheable(idea_id)

def get_latest_vote_counts():
    return VoteCount.objects.values('idea_id').annotate(max_vc=Max('votes_count'))

class IdeationListView(ListView):
    
    model = Ideation
    paginate_by = 18
    
    def get_queryset(self):
        # we don't show expired ideas so Quirky doesn't get mad
        ideas=Ideation.objects.filter(expires_at__gte=timezone.now())

        # filter for vote count
        vote_bounds=(self.request.GET.get('minvotes'), self.request.GET.get('maxvotes'))
        if vote_bounds[0] or vote_bounds[1]:
            ideas=ideas.filter(votes_count__range=vote_bounds)
        
        # filter for search text
        search_text=self.request.GET.get('search_text')
        if search_text and (self.request.GET.get('text_bool') == 'require'):
            ideas=ideas.filter(title__icontains=search_text)
        elif search_text:
            ideas=ideas.exclude(title__icontains=search_text)
        
        # filter for caps constraints
        if self.request.GET.get('allcaps') == 'exclude':
            ideas=ideas.extra(where=['title != UPPER(title)'])
        elif self.request.GET.get('allcaps') == 'require':
            ideas=ideas.extra(where=['title = UPPER(title)'])

        # figure out ordering
        order = self.request.GET.get('order_by') or 'created_at'
        if order == 'random':
            order == '?'
        if self.request.GET.get('ascending') == 'false':
            order = '-' + order          
        ideas=ideas.order_by(order)
        
        return ideas

    def get_context_data(self, **kwargs):
        context = super(IdeationListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class UserListView(ListView):
    
    model = Ideation
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def cloud(req):
    #@cached(timeout=7200)
    def _word_cloud_cached():
        ignore_words = ['/','with','the','a','if','in','it','of','or','1','-','&amp;','no','','and','for']
        title_words=' '.join(Ideation.objects.values_list('title',flat=True)).lower().split(' ')
        word_freq_counter=Counter(title_words)
        for word in ignore_words:
            if word in word_freq_counter:
                del word_freq_counter[word]
        word_freqs=word_freq_counter.most_common(200)
        # Using render_to_response rather than render because render
        # takes the request and that messes up caching. There are other
        # ways, of course.
        return render_to_response('cloud.html', {'title_cloud_data':json.dumps(word_freqs)})
        
    return _word_cloud_cached()

@csrf_exempt 
def flag(req):
    #Parse http data and create a new Flag if this IP has not clicked this before
    #try:
    idea=Ideation.objects.get(idea_id=req.POST.get('idea_id'))
    # TODO validation here, maybe using modelforms
    # check IP address in request hasn't voted on this before
    post_dict=dict(req.POST)
    post_dict={k : v[0] for k, v in post_dict.iteritems()}
    post_dict.update({'ip_address':req.META.get('REMOTE_ADDR'),'idea':idea})
    post_dict.pop('idea_id')
    print post_dict
    new_flag, created=Flag.objects.get_or_create(**post_dict)    
    #except Ideation.DoesNotExist:
        #return HttpResponseNotFound('You tried to flag an idea that does not exist.')

    # Increment the cache-like counter in the Ideation model
    if created:
        if new_flag.kind=='funny':
            idea.funny+=1
            idea.save()
        if new_flag.kind=='junk':
            idea.junk+=1
            idea.save()
    else:
        return HttpResponseForbidden('You may only flag an idea once.')
    
    return HttpResponse(json.dumps({'funny':idea.funny,'junk':idea.junk}))
    
def stats_view(req):
    plot_data=HourData.objects.values_list('start_time','new_ideas')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in plot_data])
    plot_data = '['+plot_data+']'
    return render_to_response('stats.html',{'hourly_plot_data':plot_data})