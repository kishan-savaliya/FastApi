from sqlalchemy import String,Integer,Column,DateTime,Boolean,Date
from app.database.database import Base
from app.Utils.temp_models import TempModel

class User(Base, TempModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)

    

