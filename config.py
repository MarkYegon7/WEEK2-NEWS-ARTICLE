import os 

class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY = '191743892af9cad7b309cd56ee66ad46'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
                        


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}