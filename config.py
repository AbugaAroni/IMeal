import os


class Config:
    '''
    General configuration parent class
    '''
<<<<<<< HEAD
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:2543@localhost/imeal'
=======
    SECRET_KEY = ('1201ccc5804c3210fecc')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thanos:qwerty@localhost/imeal'
>>>>>>> 0e2c201729fb816f9ba1e002455b4e421962f30f
    #heroku database below
    #SQLALCHEMY_DATABASE_URI ='postgres+psycopg2://lfgiafilewplkg:652bbbf039b88462ef1ce2fc405a8a4a434e53c197f30b192ca0ff51e636234b@ec2-3-210-255-177.compute-1.amazonaws.com:5432/d8jd2q7ohb0q7k'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


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
