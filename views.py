from django.shortcuts import render
from quirktonomicon.models import Ideation, VoteCount
from quirktonomicon.utils import dt2jsts
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse
from django.utils import simplejson
from cacheops import cached

def votes_plot(req, idea_id):
    idea=Ideation.objects.get(idea_id=idea_id)
    vote_counts=VoteCount.objects.filter(idea_id=idea_id)
    votes=vote_counts.values_list('accessed_at','votes_count')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
    return render(req, 'votes_plot.html', {'plot_data':plot_data, 'idea':idea})

@cached(timeout=7200)
def idea_json(req, idea_id):
    idea=Ideation.objects.get(idea_id=idea_id)
    vote_counts=VoteCount.objects.filter(idea_id=idea_id)
    votes=vote_counts.values_list('accessed_at','votes_count')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
    plot_data = '['+plot_data+']'
    return HttpResponse(plot_data,content_type="application/json")

def get_latest_vote_counts():
    return VoteCount.objects.values('idea_id').annotate(max_vc=Max('votes_count'))

class IdeationListView(ListView):
    
    model = Ideation
    paginate_by = 100
    
    def get_queryset(self):
        order_by = self.request.GET.get('ordering') or '-created_at'
        return Ideation.objects.filter(expires_at__gte=timezone.now()).order_by(order_by)

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

