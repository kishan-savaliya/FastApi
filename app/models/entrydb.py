from sqlalchemy import String,Integer,Column,DateTime,Boolean,ForeignKey
from database.database import Base

class Entry(Base):
    __tablename__ = 'entry_table'
    id = Column(Integer,primary_key = True,index = True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    is_delete = Column(Boolean)
    created_at = Column(DateTime,default = True)
    updated_at = Column(DateTime)
    competition_id = Column(Integer,ForeignKey('competition_id.id'))