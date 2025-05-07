from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Address(models.Model):
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=80)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=80)
    complement = models.CharField(max_length=80, blank=True, null=True)
    cep = models.CharField(max_length=9)
    class Meta:
        db_table = 'addresses'

class Discipline(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    period = models.CharField(max_length=40)
    status = models.BooleanField()
    class Meta:
        db_table = 'disciplines'

class Auth_user(AbstractUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, default='')
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=15)
    profession = models.CharField(max_length=50, default='Teacher')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'auth_users'

class User_Discipline(models.Model):
    user = models.ForeignKey(Auth_user, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    duration = models.CharField(max_length=40)
    class Meta:
        db_table = 'users_disciplines'
        unique_together = ('user', 'discipline')

class Class(models.Model):
    available_vacancies = models.IntegerField()
    name = models.CharField(max_length=50)
    class_code = models.CharField(max_length=40, unique=True)
    class Meta:
        db_table = 'classes'

class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, default='')
    email = models.EmailField()
    password = models.CharField(max_length=30)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField()
    date_of_birth = models.DateField()
    status = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'students'

class StudentDiscipline(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    registration_date = models.DateField()
    final_note = models.FloatField()
    frequency = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    class Meta:
        db_table = 'students_disciplines'
        unique_together = ('student', 'discipline')

class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    absence_date = models.DateTimeField()
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    justification = models.ForeignKey('Justification', on_delete=models.SET_NULL, null=True)
    absence_status = models.CharField(max_length=30, default='Pending')
    class Meta:
        db_table = 'absences'

class Justification(models.Model):
    submission_date = models.DateTimeField()
    desc = models.CharField(max_length=300)
    document = models.BinaryField(blank=True, null=True)
    approval_status = models.CharField(max_length=40)
    observation = models.CharField(max_length=300, blank=True, null=True)
    class Meta:
        db_table = 'justifications'

class EmployeeClass(models.Model):
    employee = models.ForeignKey(Auth_user, on_delete=models.CASCADE)
    classe = models.ForeignKey(Class, on_delete=models.CASCADE)
    class Meta:
        db_table = 'employees_classes'
        unique_together = ('employee', 'classe')

class ClassDiary(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    release_date = models.DateField()
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    employee_class = models.ForeignKey(EmployeeClass, on_delete=models.CASCADE, default=1)
    class Meta:
        db_table = 'classes_diaries'