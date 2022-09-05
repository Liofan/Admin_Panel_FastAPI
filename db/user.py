import datetime
from fastapi import Depends
from fastapi_users_db_sqlmodel import SQLModelBaseUserDB, SQLModelUserDatabase
from sqlmodel import SQLModel, Session
from core.create_session import get_session

class User(SQLModelBaseUserDB, SQLModel, table=True):
    name: str
    created_at: str = datetime.datetime.utcnow()
    updated_at: str = datetime.datetime.utcnow()

async def get_user_db(*, session: Session = Depends(get_session)):
    yield SQLModelUserDatabase(session, User)