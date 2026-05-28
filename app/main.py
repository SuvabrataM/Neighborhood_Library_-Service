from fastapi import FastAPI
from database import engine, Base

app = FastAPI(title="Neighborhood Library Service")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Library Service Running"}
