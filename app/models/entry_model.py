'''Entry model describing all entry data'''

from sqlalchemy import String,Integer,Column,DateTime,Boolean,ForeignKey
from app.database.database import Base
from datetime import datetime
from app.Utils.temp_models import TempModel
from sqlalchemy.orm import relationship

# create table of entry
class Entry(Base, TempModel):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    competition_id = Column(Integer, ForeignKey('competition.id')) # Foreign key of competition id
