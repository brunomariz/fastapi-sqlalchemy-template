import sys, os

sys.path.append(os.getcwd())

from app.db.config import DBBase, engine
from app.db.model.example_model import ExampleModel

DBBase.metadata.create_all(engine)
