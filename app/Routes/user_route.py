from fastapi import APIRouter

user = APIRouter()

@user.get('/user')
def show_user():
    return "done"

@user.post('/user')
def create_user():
    return "done"

@user.delete('/user/{id}')
def delete_user():
    return "done"

@user.put('/user/{id}')
def update_user():
    return "done"