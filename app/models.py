class Sources:
    '''
    Class that define the news sources objects 
    '''
    def __init__(self, id, name, category, description):
        self. id = id
        self.name = name
        self.category = category
        self.description = description

    
class Articles:
    '''
    Class that defines the news articles objects 
    '''
    def __init__(self, source, author, title, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author 
        self.title = title
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    