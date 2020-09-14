from redis import Redis
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from flask_bcrypt import Bcrypt

redis = Redis(host="redis", port = 6379, db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

backend = Flask(__name__)
backend.config['SECRET_KEY'] = 'fucking Strugling2makeMYLIFEworksAGAIN'


DB_USERNAME = 'root'
DB_PASSWORD = '125test'
BLOG_DATABASE_NAME = 'sqlredis'
backend.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@mysql:3306/%s?charset=utf8mb4'% (DB_USERNAME, DB_PASSWORD, BLOG_DATABASE_NAME)
backend.config['SQLALCHEMY_ECHO']=True
backend.config['SQLALCHEMY_NATIVE_UNICODE']= True

db = SQLAlchemy(backend)
fbcrypt = Bcrypt(backend)

from backend import routes


