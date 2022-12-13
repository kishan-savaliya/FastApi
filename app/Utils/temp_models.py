from app.database.database import Base
from sqlalchemy import Column,DateTime,Boolean
from datetime import datetime
    
class TempModel(object):
    created_at = Column(DateTime, default = datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.utcnow)
    is_active = Column(Boolean, default = True)
    is_delete = Column(Boolean, default = False)