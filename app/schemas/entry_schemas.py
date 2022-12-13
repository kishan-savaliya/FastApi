from pydantic import BaseModel
from datetime import date
from app.Utils.temp_schemas import TempSchema

class CreateEntry(BaseModel, TempSchema):
    title : str
    topic : str
    state : str
    country : str
    competition_id : int

class DisplayEntry(BaseModel, TempSchema):
    id : int
    title : str
    topic : str
    state : str
    country : str
    competition_id : int

    class Config():
        orm_mode = True
