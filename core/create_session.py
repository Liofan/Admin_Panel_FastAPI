from sqlmodel import Session
from db.base import engine


def get_session():
    with Session(engine) as session:
        yield session

def add_commit_refresh(session, elem):
    session.add(elem)
    session.commit()
    session.refresh(elem)