from django.shortcuts import render
from quirktonomicon.models import Ideation, VoteCount
from quirktonomicon.utils import dt2jsts

def votes_plot(req, idea_id):
    idea=Ideation.objects.get(idea_id=idea_id)
    vote_counts=VoteCount.objects.filter(idea_id=idea_id)
    votes=vote_counts.values_list('accessed_at','votes_count')
    plot_data = ','.join([r'[%.1f,%.1f]' % (dt2jsts(timestamp),value) for timestamp, value in votes])
    
    return render(req, 'votes_plot.html', {'plot_data':plot_data, 'idea':idea})
