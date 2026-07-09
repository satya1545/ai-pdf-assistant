from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("postgresql://ai_pdf_assistant_90nk_user:AjDJiGup4EpDEOqRAiOeKolHPkYpOlRK@dpg-d97shn67r5hc73dbs1gg-a.virginia-postgres.render.com/ai_pdf_assistant_90nk")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()