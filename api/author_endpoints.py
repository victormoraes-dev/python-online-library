from fastapi import FastAPI
from schemas.AuthorRequest import AuthorRequest

app = FastAPI()

@app.post("/authors/")
def create_author(author: AuthorRequest):
    """
    Create a new author.
    """

    return {"message": "Author created successfully", "author": author}