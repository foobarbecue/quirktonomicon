from quirktonomicon.models import Ideation, VoteCount, HourData
import datetime
from dateutil.tz import tzutc
from django.db.models import Max, Min

def total_active():
    return Ideation.objects.filter(expires_at__gte=datetime.datetime.now()).count()

def day_range(timestmp, before=True):
    now = datetime.datetime.now()
    if before:
        time_range = (now - timedelta(days=1), now)
    if after:
        time_range = (now, now + timedelta(days=1))
    return (before,after)

def average_vote_count_daily(time, before=True):
    mrange=day_range(time=time,before=before)
    VoteCount.objects.filter(accessed_at__range=(before,after)).aggregate(Avg('votes_count'))

def new_ideas_daily(dtime=datetime.datetime.now(), before=True):
    mrange=(dtime-datetime.timedelta(days=1),dtime)
    return Ideation.objects.filter(created_at__range=mrange).count()

def new_ideas_in_period(mrange, before=True):
    return Ideation.objects.filter(created_at__range=mrange).count()

def avg_vote_count_at_age(age):
    raise NotImplementedError

def total_votes(time):
    #The total number of votes, not double counting
    raise NotImplementedError
    

def votes_submitted(starttime, endtime):
    raise NotImplementedError

def calc_hour_stats(starttime = HourData.objects.latest().start_time, endtime = datetime.datetime.now(tzutc())):
    curtime = starttime.replace(hour=0, minute=0, second=0, microsecond=0)
    while curtime < endtime:
        mrange=(curtime, curtime+datetime.timedelta(hours=1))
        new_ideas=new_ideas_in_period(mrange)
        # TODO implement this new_ideas
        new, created = HourData.objects.get_or_create(
            start_time=curtime,
            defaults={'new_ideas':new_ideas}
            )
        if created:
            print new
        curtime+=datetime.timedelta(hours=1)

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
    
    #copy vote counts from VoteCounts to Ideations
    for k, v in votes_by_idea_in_last_day().iteritems():
        try:
            Ideation.objects.filter(idea_id=k).update(votes_in_latest_day=v)
        except Ideation.DoesNotExist:
            print "%s not in db yet" % k