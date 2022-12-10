from fastapi import APIRouter

competition = APIRouter()

@competition.get('/competition')
def show_user():
    return "done"

@competition.post('/competition')
def create_user():
    return "done"

@competition.delete('/competition/{id}')
def delete_user():
    return "done"

@competition.put('/competition/{id}')
def update_user():
    return "done"