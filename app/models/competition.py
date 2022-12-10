from sqlalchemy import String,Integer,Column,DateTime,Boolean,ForeignKey
from database.database import Base

class Competition(Base):
    __tablename__ = 'competition_table'
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String)
    status = Column(String)
    is_active = Column(Boolean)
    is_delete = Column(Boolean)
    created_at = Column(DateTime,default = True)
    updated_at = Column(DateTime)
    description = Column(String)
    user_id = Column(Integer,ForeignKey=('user_id'))