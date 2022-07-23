from app.api.v1.controllers._base import BaseController
from app.api.v1.services.example_service import ExampleService


class ExampleController(BaseController):
    def __init__(self, service=...) -> None:
        super().__init__(ExampleService())

    def example_additional_method(self):
        return self.service.example_additional_method()

    def example_index(self):
        return self.service.index()
