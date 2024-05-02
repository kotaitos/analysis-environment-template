from sqlalchemy import Column, Integer, String, DATETIME
from core.db import Base

class User(Base):
  __tablename__ = 'user'
  
  id = Column('id', Integer, primary_key=True)
  username = Column('username', String(255), nullable=False)
  created_at = Column('created_at', DATETIME, default=None)
  updated_at = Column('updated_at', DATETIME, default=None)
  deleted_at = Column('deleted_at', DATETIME, default=None)
  
  
  def to_dict(self):
    return {
      'id': self.id,
      'username': self.username,
    }
