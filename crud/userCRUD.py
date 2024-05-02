import pytz
from sqlalchemy.orm.session import Session
from core.db import engine
from models import User
from datetime import datetime

class userCRUD:
  @staticmethod
  def create(user: User) -> User:
    user.created_at = datetime.now(pytz.timezone('Asia/Tokyo'))
    with Session(engine) as session:
      session.add(user)
      session.commit()
      session.refresh(user)
      return user
  
  @staticmethod
  def read(id: int) -> User:
    with Session(engine) as session:
      user = session.get(User, id)
      if user and user.deleted_at is None:
        return user
      return None
    
  @staticmethod
  def read_all() -> list[User]:
    with Session(engine) as session:
      users = session.query(User).filter(User.deleted_at == None).all()
      return users
    
  @classmethod
  def update(user: User) -> User:
    user.updated_at = datetime.now(pytz.timezone('Asia/Tokyo'))
    with Session(engine) as session:
      session.add(user)
      session.commit()
      session.refresh(user)
      return user
  
  @staticmethod
  def delete(id: int) -> None:
    with Session(engine) as session:
      user = session.get(User, id)
      if user:
        user.deleted_at = datetime.now()
        session.add(user)
        session.commit()
