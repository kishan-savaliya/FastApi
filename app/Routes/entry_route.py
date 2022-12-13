from fastapi import APIRouter,Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.entry_model import Entry
from app.schemas.entry_schemas import CreateEntry,DisplayEntry
from typing import List

entry = APIRouter()

@entry.get('/allentry', response_model = List[DisplayEntry], tags=['entry'])
def show_entry(db:Session = Depends(get_db)):
    all_entry = db.query(Entry).all()
    return all_entry

@entry.get('/entry/{id}', response_model = DisplayEntry, tags=['entry'])
def show_entry(id, db: Session = Depends(get_db)):
    new_entry = db.query(Entry).filter(Entry.id == id).first()
    return new_entry

@entry.post('/entry', response_model = DisplayEntry, tags=['entry'])
def create_entry(request: CreateEntry, db: Session = Depends(get_db)):
    new_entry = Entry(title = request.title, topic = request.topic, state = request.state, country = request.country, competition_id = request.competition_id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@entry.delete('/entry/{id}', tags=['entry'])
def delete_entry(id, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

@entry.put('/entry/{id}', tags=['entry'])
def update_entry(id, request: CreateEntry, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).update(request.dict())
    db.commit()
    return "updated"