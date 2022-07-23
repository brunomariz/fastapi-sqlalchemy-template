from app.api.v1.services._base import BaseService
from app.db.model.example_model import ExampleModel


class ExampleService(BaseService):
    def __init__(self) -> None:
        super().__init__(model=ExampleModel)

    def example_additional_method(self):
        return {"method": "example additional method"}

    def index(self):
        print("oi")
        return self.session.query(self.model).all()
