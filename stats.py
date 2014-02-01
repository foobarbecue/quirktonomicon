from quirktonomicon.models import Ideation, VoteCount
import datetime
from django.db.models import Max, Min

def total_active():
    return Ideation.objects.filter(expires_at__gte=datetime.datetime.now()).count()
    
def average_vote_count_daily(datetime, before=True):
    now = datetime.datetime.now()
    if before:
        time_range = (now - timedelta(days=1), now)
    if after:
        time_range = (now, now + timedelta(days=1))
    VoteCount.objects.filter(accessed_at__range=('2014-01-24','2014-01-25')).aggregate(Avg('votes_count'))

def avg_vote_count_at_age(age):
    raise NotImplementedError

def total_votes(time):
    #The total number of votes, not double counting
    raise NotImplementedError
    

def votes_submitted(starttime, endtime):
    raise NotImplementedError

def votes_by_idea_in_last_day():
    now=datetime.datetime.now()
    last_day=(now-datetime.timedelta(days=1),now)
    vote_max_mins=VoteCount.objects.filter(accessed_at__range=last_day)\
        .values('idea_id')\
        .order_by('idea_id')\
        .annotate(max_vc=Max('votes_count'),min_vc=Min('votes_count'))
    #votes_in_day={v['idea_id']:v['max_vc']-v['min_vc'] for v in vote_max_mins}
    votes_in_day={v['idea_id']:v['max_vc']-v['min_vc'] for v in vote_max_mins if v['max_vc'] != v['min_vc']}

    return votes_in_day

def update():
    for k, v in votes_by_idea_in_last_day().iteritems():
        try:
            Ideation.objects.filter(idea_id=k).update(votes_in_latest_day=v)
        except Ideation.DoesNotExist:
            print "%s not in db yet" % k