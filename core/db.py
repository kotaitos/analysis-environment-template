import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# 環境変数から取得する
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

DATABASE = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8'

engine = create_engine(DATABASE)

Base = declarative_base()
