from concurrent.futures import process
from unicodedata import category
import urllib.request,json
from .models import Sources
from .models import Articles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCES_URL']

def get_sources():
    '''
    Function that gets json response
    '''

    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=c3011dcec4e546228a335c5326e69378'
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources (sources_results_list)

    return sources_results

def process_sources (sources_list):
    '''
    Function that processes the source results and transforms to objects
    '''

    sources_results = []
    for sources_items in sources_list:
        #  id, name, category, description) 
        id = sources_items.get('id')
        name = sources_items.get('name')
        category = sources_items.get('category')
        description = sources_items.get('description')

        if id: 
            sources_objects = Sources(id, name, category, description)

            sources_results.append(sources_objects)
    
    return sources_results

def get_articles ():
    '''
    A function that gets a response for the articles body
    '''
    get_articles_url = 'https://newsapi.org/v2/articles?apiKey=c3011dcec4e546228a335c5326e69378'
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read ()
        get_articles_response = json.loads(get_articles_data)
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles (articles_results_list)
    
    return articles_results


def process_articles (articles_list):
    '''
    Fuction that processes what the articles results are and transforms them to objects 
    '''
    articles_results = []
    for articles_items in articles_list:
        source = articles_items.get('source')
        author = articles_items.get('author')
        title = articles_items.get('title')
        url = articles_items.get('url')
        urlToImage = articles_items.get('urlToImage')
        publishedAt  = articles_items.get('publishedAt')
        content = articles_items.get('content')

        if source:
            articles_objects = Articles(author, title, url, urlToImage, publishedAt, content)

            articles_results.append(articles_objects)

    
    return articles_results

