from fastapi import FastAPI , status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

# Crude operation

app = FastAPI()

anime_list = [
  {
    "id": 1,
    "title": "Naruto",
    "author": "Masashi Kishimoto"
  },
  {
    "id": 2,
    "title": "One Piece",
    "author": "Eiichiro Oda"
  },
  {
    "id": 3,
    "title": "Attack on Titan",
    "author": "Hajime Isayama"
  },
  {
    "id": 4,
    "title": "Death Note",
    "author": "Tsugumi Ohba"
  },
  {
    "id": 5,
    "title": "Demon Slayer",
    "author": "Koyoharu Gotouge"
  }
]

@app.get('/animes')
def all_Anime():
    return anime_list

class Anime(BaseModel):
    title: str
    author:str

# Create 
@app.post("/create_anime/")
def create_book(anime:Anime):
    newAnime = {
    "id": len(anime_list) + 1,
    "key": anime.model_dump()
    }
    anime_list.append(newAnime)
    return {"Message": "Book created successfully"}


# Read
@app.get('/find_anime/{anime_id}')
def find_anime(anime_id: int):
    for anime in anime_list:
        if anime['id'] == anime_id:
            return anime

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found!")


# Update 
@app.put('/anime/{anime_id}')
def update_anime(anime_id: int,update_anime: Anime):
    for anime in anime_list:
        if anime['id'] == anime_id:
            anime['title'] = update_anime.title
            anime['author'] = update_anime.author
            return {"Message": "Update successfully"}
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found!")


# Delete
@app.delete('/delete_anime/{anime_id}')
def delete_anime(anime_id: int):
    for anime in anime_list:
        if anime['id'] == anime_id:
            anime_list.remove(anime)
            return {"Message": "Deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anime not found!")
