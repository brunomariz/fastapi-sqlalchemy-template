from app.db.config import db_session


class BaseService:
    def __init__(self, model):
        self.session = db_session
        self.model = model

    def index(self):
        return [{"message": "mock base index"}]
