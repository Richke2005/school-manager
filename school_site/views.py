from django.shortcuts import render
import json
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Auth_user, Student
from .services import ClassService, UserService

# Create your views here.
def forgot_password_view(request):
    return render(request, 'auth/forgot_password/forgot_password.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def user_profile_view(request):
    try:
        user_data = Auth_user.objects.get(id=1)
        return render(request, 'user/profile/profile.html', {'user': user_data})
    except Auth_user.DoesNotExist:
        raise Http404("User does not exist")

@login_required
def users_management_view(request):
    if request.method == 'GET':
        users_data = UserService().get_all()
        return render(request, 'manager/users_management/users.html', {'users': users_data})
    
@login_required
def classes_view(request):
    class_data = ClassService().get_all()
    return render(request, 'classes/classes.html', {'classes': class_data})

@login_required
def students_by_class_view(request, class_id):
    try:
        students_data = Student.objects.filter(student_class=class_id)
        return render(request, 'classes/students_of_class.html', {'students': students_data})
    except Student.DoesNotExist:
        raise Http404("Student does not exist")

