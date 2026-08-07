from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class Anime(BaseModel):
    id: int
    title: str
    author: str

@app.get("/anime")
def get_anime(db: Session = Depends(get_db)):
    books = db.query(model.Anime_model).all()
    return books

@app.post('/create')
def create_list(a:Anime, db: Session= Depends(get_db)):
    new_Anime = model.Anime_model(id=a.id,title=a.title,author=a.author)
    db.add(new_Anime)
    db.commit()
    db.refresh(new_Anime)
    return {"Message": "Data Added Successfully"}
    