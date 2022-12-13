from fastapi import APIRouter, Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schemas import CreateUser, DisplayUser
from typing import List

user = APIRouter()

@user.get('/alluser', response_model = List[DisplayUser], tags=['user'])
def show_user(db: Session = Depends(get_db)):
    all_user = db.query(User).all()
    return all_user

@user.get('/user/{id}', response_model = DisplayUser, tags=['user'])
def show_user(id,db: Session = Depends(get_db)):
    new_user = db.query(User).filter(User.id == id).first()
    return new_user

@user.post('/user', response_model = DisplayUser, tags=['user'])
def create_user(request: CreateUser, db: Session = Depends(get_db)):
    new_user = User(name = request.name, birth_date = request.birth_date, gender = request.gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.delete('/user/{id}', tags=['user'])
def delete_user(id, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

@user.put('/user/{id}', tags=['user'])
def update_user(id, request: CreateUser, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).update(request.dict())
    db.commit()
    return "Updated"