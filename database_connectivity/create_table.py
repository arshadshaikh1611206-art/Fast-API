from database import Base, engine
from model import Anime_model

# Take all my SQLAlchemy models and create those tables in the database using this engine.
Base.metadata.create_all(bind=engine)