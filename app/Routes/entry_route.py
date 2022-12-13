'''Entry routes to perform crud operation'''

from fastapi import APIRouter,Depends
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.entry_model import Entry
from app.models.competition_model import Competition
from app.schemas.entry_schemas import CreateEntry,DisplayEntry
from typing import List

entry = APIRouter()

# show all entry data
@entry.get('/allentry', response_model = List[DisplayEntry], tags=['entry'])
def show_entry(db:Session = Depends(get_db)):
    all_entry = db.query(Entry).all()
    return all_entry

# show specific user by id
@entry.get('/entry/{id}', response_model = DisplayEntry, tags=['entry'])
def show_entry(id, db: Session = Depends(get_db)):
    new_entry = db.query(Entry).filter(Entry.id == id).first()
    return new_entry

# create new entry using post method
@entry.post('/entry', response_model = DisplayEntry, tags=['entry'])
def create_entry(request: CreateEntry, db: Session = Depends(get_db)):
    new_entry = Entry(title = request.title, topic = request.topic, state = request.state, country = request.country, competition_id = request.competition_id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

# Delete entry by id
@entry.delete('/entry/{id}', tags=['entry'])
def delete_entry(id, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

# Update the entry by id
@entry.put('/entry/{id}', tags=['entry'])
def update_entry(id, request: CreateEntry, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).update(request.dict())
    db.commit()
    return "updated"

@entry.get('/entry/{UserId}/count')
def count_user(UserId, db: Session = Depends(get_db)):
    competitions = db.query(Competition.id).filter(Competition.user_id == UserId).all()

    competitions = [competition.id for competition in competitions]
    # return competitions

    result = 0
    for competition in competitions:
        # print(competition)
        entry = db.query(Entry).filter(Entry.competition_id == competition).count()
        # print(entry)
        result += entry
    return result
