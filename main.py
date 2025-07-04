from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from api.handler.exception_handler import validation_exception_handler
from api.author_endpoints import author_router 
from database_config.database_configuration import Base
from database_config.database_configuration import engine
from database_config.models.author import Author

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(author_router)
app.add_exception_handler(RequestValidationError, validation_exception_handler)