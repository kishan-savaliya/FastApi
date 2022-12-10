from sqlalchemy import String,Integer,Column,DateTime,Boolean
from database.database import Base

class User(Base):
    __tablename__ = 'user_table'
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String)
    birth_date = Column(String)
    gender = Column(String)
    created_at = Column(DateTime,default = True)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)
    is_delete = Column(Boolean)