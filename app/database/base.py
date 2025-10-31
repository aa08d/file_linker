from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


class Base(DeclarativeBase):
  	pass


engine = create_engine("sqlite:///db.sqlite3")
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session() -> Session:
		return SessionLocal()

def init_db() -> None:
  	Base.metadata.create_all(bind=engine)
