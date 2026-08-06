from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Get Method

@app.get('/')
def home():
    return {"Message": "Hello world"}

@app.get('/about/{age}')
def about(age: int):
    return {"Message": f"Hello john your age is {age}"}

@app.get('/blog/{name}')
def blog(name:str,age: Optional[int]=10):
    return {"Message": f"Hello {name} your age is {age}"}

# Post Method

class Zoo(BaseModel):
    Wanimal: int
    Danimal: int

@app.post('/animals')
def animals(zoo: Zoo):
    return {
        "W-animal": zoo.Wanimal,
        "D-animal": zoo.Danimal,
        "Number-of-Total-Animal": zoo.Wanimal + zoo.Danimal
    }