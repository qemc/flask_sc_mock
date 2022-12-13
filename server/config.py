import redis

class ApplicationConfig():

    SECRET_KEY = '6be575743c714c0250e548de'
    #PC
    SQLALCHEMY_DATABASE_URI =  'sqlite:///C:/Users/Grzegorz/Documents/Programing/flask_template/quotesv2/instance/db.db'  
    #laptop 
    #SQLALCHEMY_DATABASE_URI =  'sqlite:///db.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")