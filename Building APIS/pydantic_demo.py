from fastapi import FastAPI
from pydantic import BaseModel

class user(BaseModel):
    id:int
    name:str

app=FastAPI()

@app.get('/user',response_model=user)
def get_user():
    return user(id=1,name='Bruce')