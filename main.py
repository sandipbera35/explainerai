import uvicorn
from fastapi import FastAPI

app = FastAPI()
    
@app.get("/")
def root():
    world_ = {"message": "Hello World"}
    return world_

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"} 

if __name__ == "__main__":  
    uvicorn.run(app, host="127.0.0.1", port=8000)

