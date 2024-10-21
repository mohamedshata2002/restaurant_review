from fastapi import FastAPI 
from app.routers import restaurant

app = FastAPI()

@app.get("/")
def test():
    return {"Hello world"}
app.include_router(restaurant.router)