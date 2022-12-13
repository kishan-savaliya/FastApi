from pydantic import BaseModel,Field
from datetime import date
from app.Utils.temp_schemas import TempSchema

# class Users(BaseModel):
#     id : int
#     name : str
#     birth_date : date
#     gender : str
    

class CreateUser(BaseModel, TempSchema):
    name: str
    birth_date: date = Field(default_factory = date(2022,12,12))
    gender: str

class DisplayUser(BaseModel, TempSchema):
    id : int
    name: str
    birth_date: date
    gender: str

    class Config():
        orm_mode = True

