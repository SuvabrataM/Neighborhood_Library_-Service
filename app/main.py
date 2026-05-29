from fastapi import FastAPI
from database import engine, Base

from routes import books, members

app = FastAPI(title="Neighborhood Library Service")

Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(members.router)

@app.get("/")
def home():
    return {"message": "Library Service Running"}
