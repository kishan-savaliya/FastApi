from pydantic import BaseModel

class Competition(BaseModel):
    id : int
    title : str
    topic : str
    state : str
    is_delete : str
    country : str
    created_at : int
    updated_at : int
    competition_id : int