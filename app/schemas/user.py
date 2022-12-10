from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    birth_date : str
    gender : str
    created_at : int
    updated_at : int
    is_active : str
    is_delete : str