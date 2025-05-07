from zoneinfo import available_timezones

from django.test import TestCase
from .services.student_service import StudentService
from .models import Student, Address, Class  # Assuming you have a Student model defined in models.py
from datetime import datetime

class StudentDataTest(TestCase):
    def setUp(self):
        # Create mock Address and Class objects
        address = Address.objects.create(
            street="123 Test St",
            city="Test City",
            state="TS",
            cep="12345",
            number=51
        )
        student_class = Class.objects.create(
            name="Test Class",
            class_code="03AN",
            available_vacancies=30
        )

        # Create mock Students
        Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            password="testpassword",
            rg="123456789",
            cpf="11122233344",
            phone_number="1234567890",
            registration_date=datetime.now(),
            date_of_birth="2000-01-01",
            status=True,
            address=address,
            class_key=student_class
        )
        Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="janesmith@example.com",
            password="testpassword",
            rg="987654321",
            cpf="55566677788",
            phone_number="0987654321",
            registration_date=datetime.now(),
            date_of_birth="1998-05-12",
            status=False,
            address=address,
            class_key=student_class
        )


    async def testing_all_students(self):
        # Call the get_all() method from the service
        all_data = await StudentService().get_all()

        # Retrieve all students directly from the database
        expected_data = list(Student.objects.values())

        # Ensure that the retrieved data matches the data in the database
        self.assertEqual(list(all_data), expected_data)
