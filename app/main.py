from fastapi import FastAPI
from app.database import engine, Base
from app.routes import books, members, borrow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Neighborhood Library Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(members.router)
app.include_router(borrow.router)

@app.get("/")
def home():
    return {"message": "Neighborhood Library Service Running"}
