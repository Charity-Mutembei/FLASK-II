# from turtle import title
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
from ..requests import get_articles
# from .forms import ReviewForm
# from ..models import Sources

# Views
@main.route('/')
def index():
    '''
    Rootpage function that returns the index page and its data
    '''

    sources = get_sources()
    articles = get_articles()
    # articles = get_articles()

    title = 'News Today' 

    return render_template('index.html', title = title, sources = sources,articles = articles)

@main.route('/articles')
def articles ():
    '''
    Function that returns the article page and its data
    '''
    articles = get_articles()
    title = 'Articles Today' 

    return render_template('articles.html', title = title, articles = articles)