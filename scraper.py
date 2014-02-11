import requests, datetime, os
import simplejson as json
from django import db
from django.core import serializers
from quirktonomicon.models import Ideation, VoteCount
from quirktonomicon import stats

def get_ideas_from_api(sort='newest',categories='all',start=0,end=50,per_request=10):
    # Quirky website sends requests with limit=26 but changing the limit parameter
    # seems to have no effect.
    ideas=[]
    try:
        for reqnum in range((end-start)/per_request):
            offset=start+reqnum*per_request
            params={'sort':sort,'offset':offset,'limit':per_request}
            print 'offset %s' % offset
            data=requests.get('http://www.quirky.com/api/v2/ideations/filtered_ideations.json',params=params).json()['data']
            ideas+=data['ideations']
    except:
        print 'fail on reqnum ' + str(reqnum)
    return ideas

def scrape_to_file(start=0,end=10000):
    with open('/home/aaron/quirktonomicon/scrape/%sfor%sto%s.txt' % (str(datetime.datetime.utcnow()),start,end),'w') as f:
        f.write(str(get_ideas_from_api(start=start,end=end)))

def read_json(ideas_string):
    json.loads()

def write_idea_to_db(idea_dict, accessed_at):
    # idea should be a dict containing one "ideation"
    idea_id = idea_dict.pop('idea_id')
    idea, created = Ideation.objects.get_or_create(defaults=idea_dict, idea_id=idea_id)
    if not created:
        # Already existed, so we don't need to re-save the description etc, instead we make a "vote count"
        vote_count_params  = ['votes_count',
                              'total_votes_needed',
                              'considered_at',
                              'state',]
        vote_count_par_dict = { key : idea_dict[key] for key in vote_count_params }
        vote_count_par_dict.update({'idea_id':idea_id})
        VoteCount.objects.create(accessed_at = accessed_at, **vote_count_par_dict)
        #Update the current vote count on the Ideation as well. This is redundant, a sort of cache.
        idea.votes_count=vote_count_par_dict['votes_count']
        idea.funny=0
        idea.junk=0
        idea.save()
    
def ideas_api_to_db(**kwargs):
    ideas=get_ideas_from_api(**kwargs)
    for idea in ideas:
        write_idea_to_db(idea, accessed_at = datetime.datetime.now())
        db.reset_queries()
    stats.update()

def scraped_file_to_db(filename):
    basepath=os.getcwd()
    try:
        with open(filename) as f:
            # Temporary solution. Should use actual json
            exec('ideas = ' + f.read())
            # Get accessed 
            for idea in ideas:
                accessed_at = datetime.datetime.strptime(filename.split('.')[0], '%Y-%m-%d %H:%M:%S')
                write_idea_to_db(idea, accessed_at = accessed_at)
                try:
                    os.rename(basepath + '/' + filename, basepath + '/in_db/' + filename)
                except OSError:
                    pass
    except:
        print 'fail on ' + filename
        return -1
