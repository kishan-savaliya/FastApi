from fastapi import APIRouter

entry = APIRouter()

@entry.get('/entry')
def show_user():
    return "done"

@entry.post('/entry')
def create_user():
    return "done"

@entry.delete('/entry/{id}')
def delete_user():
    return "done"

@entry.put('/entry/{id}')
def update_user():
    return "done"