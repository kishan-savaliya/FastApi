from pydantic import BaseModel
from datetime import date
from app.Utils.temp_schemas import TempSchema

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
