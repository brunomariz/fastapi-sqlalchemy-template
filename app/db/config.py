import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    os.environ["DB_URI"],
    pool_pre_ping=True,
    # connect_args={"check_same_thread": False},
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DBBase = declarative_base()
