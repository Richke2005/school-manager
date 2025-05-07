from .service import Service
from ..models import Student

class StudentService(Service):
    def __init__(self):
        super().__init__(Student)