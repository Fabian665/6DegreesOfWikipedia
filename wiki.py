import wikipedia
import requests
import time
from datetime import datetime


API_URL = 'http://en.wikipedia.org/w/api.php'
RATE_LIMIT = False
RATE_LIMIT_MIN_WAIT = None
RATE_LIMIT_LAST_CALL = None
USER_AGENT = 'fabianro@post.bgu.ac.il'


def wiki_request(params):
    """
    Make a request to the Wikipedia API using the given search parameters.
    Returns a parsed dict of the JSON response.
    """
    global RATE_LIMIT_LAST_CALL
    global USER_AGENT

    params['format'] = 'json'

    if 'action' not in params:
        params['action'] = 'query'

    headers = {
        'User-Agent': USER_AGENT
    }

    if RATE_LIMIT and RATE_LIMIT_LAST_CALL and RATE_LIMIT_LAST_CALL + RATE_LIMIT_MIN_WAIT > datetime.now():

        # it hasn't been long enough since the last API call
        # so wait until we're in the clear to make the request

        wait_time = (RATE_LIMIT_LAST_CALL + RATE_LIMIT_MIN_WAIT) - datetime.now()
        time.sleep(int(wait_time.total_seconds()))

    r = requests.get(API_URL, params=params, headers=headers)

    if RATE_LIMIT:
        RATE_LIMIT_LAST_CALL = datetime.now()

    return r.json()


def search(query):
    params = {
        'list': 'search',
        'srprop': '',
        'srlimit': 1,
        'srsearch': query
    }

    result = wiki_request(params)['query']['search'][0]

    return result['title'], result['pageid']


# print(search("Barack Obama"))


ny = wikipedia.search("New York City", results=1, suggestion=False)
# print(dir(ny[0]))
print(dir(wikipedia.WikipediaPage(pageid=1874)))
