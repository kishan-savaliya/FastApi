from pydantic import BaseModel

class Competition(BaseModel):
    id : int
    name : str
    status : str
    is_active : str
    is_delete : str
    description : str
    created_at : int
    updated_at : int
    user_id : int