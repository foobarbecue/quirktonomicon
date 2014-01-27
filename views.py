from django.shortcuts import render
from quirktonomicon.models import Ideation, VoteCount
from quirktonomicon.utils import dt2jsts
from django.views.generic.list import ListView
from django.utils import timezone

def votes_plot(req, idea_id):
    idea=Ideation.objects.get(idea_id=idea_id)
    vote_counts=VoteCount.objects.filter(idea_id=idea_id)
    votes=vote_counts.values_list('accessed_at','votes_count')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
    
    return render(req, 'votes_plot.html', {'plot_data':plot_data, 'idea':idea})

def get_latest_vote_counts():
    return VoteCount.objects.values('idea_id').annotate(max_vc=Max('votes_count'))

class IdeationListView(ListView):
    
    model = Ideation
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context