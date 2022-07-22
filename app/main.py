from fastapi import FastAPI
from app.api.v1.routes.example_router import example_router
from app.db.config import engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example_router)


@app.get("/")
def health_check():
    return {"message": "health check"}


@app.get("/hello")
def hello():
    return {"message": "hello, world!"}
