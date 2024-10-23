from fastapi import FastAPI 
from app.routers import restaurant ,users ,login ,reservation,review

app = FastAPI()

@app.get("/")
def test():
    return {"Hello world"}
app.include_router(restaurant.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(reservation.router)

app.include_router(review.router)