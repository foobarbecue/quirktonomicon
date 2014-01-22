import requests, datetime
import simplejson as json
from quirktonomicon.models import Ideation

def get_ideas_from_api(sort='newest',categories='all',start=0,end=50,per_request=10):
    # Quirky website sends requests with limit=26 but changing the limit parameter
    # seems to have no effect.
    ideas=[]
    for reqnum in range((end-start)/per_request):
        offset=start+reqnum*per_request
        params={'sort':sort,'offset':offset,'limit':per_request}
        # 26 seems to be maximum for limit
        print 'offset %s' % offset
        data=requests.get('http://www.quirky.com/api/v2/ideations/filtered_ideations.json',params=params).json()['data']
        ideas+=data['ideations']
    return ideas

def scrape_to_file(start=0,end=10000):
    with open('/home/aaron/quirktonomicon/scrape/%sfor%sto%s.txt' % (str(datetime.datetime.utcnow()),start,end),'w') as f:
        f.write(str(get_ideas_from_api(start=start,end=end)))

def read_json(ideas_string):
    json.loads()

def write_idea_to_db(idea):
    # idea should be a dict containing one "ideation"
    idea_id=idea.pop('idea_id')
    Ideation.objects.get_or_create(defaults=idea, idea_id=idea_id)
