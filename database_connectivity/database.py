from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# loading .ENV file 
load_dotenv()
# Go look inside the environment and return the value of DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

## Here engine get the URl of our mySQL fast_API databse
engine = create_engine(DATABASE_URL)

# Session use to handle task like db.add(), db.query(), db.commit() etc... Its an working connection to db
sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine) # here we are saying it to use our engine 

# Base use to define databse table
Base = declarative_base()

# This function is used to open session, do their work and close it
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
