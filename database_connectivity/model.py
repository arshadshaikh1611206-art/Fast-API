from database import Base
from sqlalchemy import Column, Integer, VARCHAR

class Anime_model(Base):
    __tablename__ = "animes"

    id = Column(Integer,primary_key=True,unique=True,index=True)
    title = Column(VARCHAR(50))
    author = Column(VARCHAR(20))