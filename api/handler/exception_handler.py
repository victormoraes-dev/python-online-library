from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from api.schemas.GenericResponse import GenericResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    
    """
    Custom exception handler for request validation errors.
    Returns a JSON response with the error details.
    """

    error_type = exc.errors()[0]['type']
    error_message = exc.errors()[0]['msg']
    
    return JSONResponse(
        status_code=422,
        content=GenericResponse(
            data=None,
            error_message={"type": error_type, "message": error_message},
        ).model_dump(exclude_none=True))