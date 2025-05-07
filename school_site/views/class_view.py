from .base_view import BaseView
from ..services import ClassService
from django.shortcuts import render
from django.http import JsonResponse


class_service = ClassService()

class ClassView(BaseView):
    def __init__(self, template_name: str = None):
        super().__init__(template_name, class_service)

    def load_my_classes_view(self, request):
        """
        Load the classes view with the list of classes for the user.
        """
        if request.method == 'GET':
            user = request.user
            try:
                classes = class_service.get_classes_by_user(user)
                print(classes.values())
                return render(request, self.template_name, {"data": classes})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
            
    def load_class_students_view(self, request, id):
        """
        Load the class students view with the list of students in the class.
        """
        if request.method == 'GET':
            try:
                students = class_service.get_students_by_class_id(id)
                print(students)
                return render(request, "user/classes/students_of_class.html", {"data": students})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)

