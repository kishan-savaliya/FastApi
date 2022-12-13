from pydantic import BaseModel
from datetime import date
from app.Utils.temp_schemas import TempSchema

# class Competition(BaseModel):
#     id : int
#     name : str
#     status : str
#     description : str
#     user_id : int

class CreateCompetition(BaseModel, TempSchema):
    name : str
    status : bool
    description : str
    user_id : int

class DisplyCompetition(BaseModel, TempSchema):
    id : int
    name : str
    status : bool
    description : str
    user_id : int

    class Config():
        orm_mode = True

