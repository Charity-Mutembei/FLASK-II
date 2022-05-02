import os

class Config:

    NEWS_API_SOURCES_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = 'c3011dcec4e546228a335c5326e69378'
    SECRET_KEY = 'charity'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}