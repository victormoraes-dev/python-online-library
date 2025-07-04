from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse

from api.schemas.AuthorRequest import AuthorRequest
from api.schemas.AuthorResponse import AuthorResponse
from api.schemas.GenericResponse import GenericResponse

from sqlalchemy.orm import Session

from database_config.database_session_config import get_db
from database_config.database_configuration import engine
from database_config.models.author import Author
from database_config.models import author

author_router = APIRouter()

@author_router.post("/authors/", status_code=status.HTTP_201_CREATED, response_model=GenericResponse)
def create_author(author: AuthorRequest, db: Session = Depends(get_db)):
    """
    Create a new author.
    """

    try:

        author_data = Author(
            name=author.name,
            email=author.email,
            description=author.description
        )

        db.add(author_data)
        db.commit()
        db.refresh(author_data)

        author_response = AuthorResponse.model_validate(author_data, from_attributes=True)
        
        return GenericResponse(data={"message": "Author created successfully", "author": author_response})
    except Exception as e:

        error_message={"type": "internal server error", "message": str(e)}
        return JSONResponse(
            status_code=500,
            content=GenericResponse(data=None, 
                                    error_message=error_message)
                                    .model_dump(exclude_none=True))