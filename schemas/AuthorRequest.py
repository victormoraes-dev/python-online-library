## Here, I will use the `pydantic` library to define a model for author requests.
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class AuthorRequest(BaseModel):
    """
    Model representing an author request.
    """
    name: str = Field(..., description="Name of the author", min_length=3)
    email: str = Field(..., description="Email of the author", min_length=5, max_length=254)
    description: Optional[str] = Field(None, description="Description of the author", max_length=400)