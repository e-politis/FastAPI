from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


#query parameters   limit=10&published=true
@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None ): #validate "published var" because its string

    #only get 10 published blogs  
    if published:
        return {"data": f'{limit} published blogs from db'}
    else: 
        return {"data": f'{limit} blogs from db'}


#path parameters
@app.get('/blog/unpublished')       # this should be above {id} <-- dynamic routing 
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def commets(id):
    return {'comments': {'1', '2'}}

#model
class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with title as {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)