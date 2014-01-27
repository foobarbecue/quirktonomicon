from quirktonomicon.models import Ideation, VoteCount
import datetime

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
    

def total_votes(time):
    #The total number of votes, not double counting
    

def votes_submitted(starttime, endtime):
    