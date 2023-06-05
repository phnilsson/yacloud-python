import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Hejsan123@mysql/traininglog'
    #SQLALCHEMY_DATABASE_URI = os.getenv('CONNECTIONSTRING')
    SECRET_KEY = "SECRET_KEY"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    DEBUG = True
    SECRET_KEY = "SECRET_KEY"
