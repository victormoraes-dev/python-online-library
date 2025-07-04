from pydantic import BaseModel, Field
from typing import Optional, Any

class GenericResponse(BaseModel):

    data: Optional[Any] = Field(None, description="Data returned in the response, if any")
    error_message: Optional[dict[str, Any]] = Field(None, description="Error message if an error occurred")