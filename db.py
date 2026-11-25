from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://project_95yb_user:SFrX3Kh9YvvgX2LpUQfWx1qas94IOOOP@dpg-dc38768m7kps73dgh21g-a.oregon-postgres.render.com/project_95yb"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
