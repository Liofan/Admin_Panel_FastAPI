from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from core.create_session import get_session, add_commit_refresh
from core.security import hash_password
from db.base import engine
from db.user import User
from schema.users import User as schema_user
from schema.users import UserIn as schema_user_add

router = APIRouter()

@router.get('', name='Список всех пользователй', status_code=200, response_model=List[schema_user])
async def get_all(*, session: Session = Depends(get_session), limit: int = 100, skip: int = 0) -> list:
    all_user = select(User).limit(limit).offset(skip)
    return session.exec(all_user).all()

@router.get('/{id}', name="Получить пользователя по ID", status_code=200)
async def get_by_id(*, session: Session = Depends(get_session), id: int) -> Optional[User]:
    query = select(User).where(User.id == id)
    return session.exec(query)

@router.post('/add', name='Добавление пользователя', status_code=200)
async def add_codes(*, session: Session = Depends(get_session), add: schema_user_add):
    user = User(name=add.name, email=add.email, hashed_password=hash_password(add.password))
    add_commit_refresh(session, user)
    return user
