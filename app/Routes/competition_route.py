'''competition routes to perform crud operation'''

from fastapi import APIRouter, Depends
from app.database.database import get_db
from app.models.competition_model import Competition
from app.schemas.competition_schemas import CreateCompetition,DisplyCompetition
from sqlalchemy.orm import Session
from typing import List

competition = APIRouter()

# show all competition data
@competition.get('/allcompetition', response_model = List[DisplyCompetition], tags=['competition'])
def show_competition(db: Session = Depends(get_db)):
    new_competition = db.query(Competition).all()
    return new_competition

# show specific competition by id
@competition.get('/competition/{id}', response_model = DisplyCompetition, tags=['competition'])
def show_competition(id, db: Session = Depends(get_db)):
    new_competition = db.query(Competition).filter(Competition.id == id).first()
    return new_competition

# create new competition using post method
@competition.post('/competition', response_model = DisplyCompetition, tags=['competition'])
def create_competition(request: CreateCompetition,db: Session = Depends(get_db)):
    new_competition = Competition(name = request.name, status = request.status, description = request.description, user_id = request.user_id)
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)
    return new_competition

# Delete competition by id
@competition.delete('/competition/{id}', tags=['competition'])
def delete_competition(id, db: Session = Depends(get_db)):
    db.query(Competition).filter(Competition.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"

# update competition by id using put method
@competition.put('/competition/{id}',tags=['competition'])
def update_competition(id, request: CreateCompetition, db: Session = Depends(get_db)):
    db.query(Competition).filter(Competition.id == id).update(request.dict())
    db.commit()
    return "updated"
