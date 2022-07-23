from app.api.v1.services._base import BaseService
from app.db.model.example_model import ExampleModel


class BaseController:
    def __init__(self, service=BaseService(model=...)) -> None:
        self.service = service

    def index(self):
        return self.service.index()
