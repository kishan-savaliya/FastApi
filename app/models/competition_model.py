'''competition model describing all competition data'''

from sqlalchemy import String,Integer,Column,DateTime,Boolean,ForeignKey
from app.database.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.Utils.temp_models import TempModel

# create table of competition
class Competition(Base,TempModel):
    __tablename__ = 'competition'
    id = Column(Integer,primary_key = True,index = True, autoincrement = True)
    name = Column(String)
    status = Column(Boolean)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id')) # Foreign key of user id
