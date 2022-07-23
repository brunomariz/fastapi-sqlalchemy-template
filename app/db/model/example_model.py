from sqlalchemy import Column, Integer, String
from app.db.config import DBBase


class ExampleModel(DBBase):
    __tablename__ = "EXAMPLE"

    ID = Column(Integer, primary_key=True)
    EXAMPLE_MSG = Column(String)
