from .service import Service
from ..models import Class

class ClassService(Service):
    def __init__(self):
        super().__init__(Class)
    
    def get_classes_by_user(self, user):
        """
        Get all classes for a teacher.
        """
        return self.model.objects.filter(employeeclass__employee=user).distinct()
    
    def get_students_by_class_id(self, class_id):
        """
        Get all students for a class.
        """
        return self.model.objects.filter(id=class_id).prefetch_related('student').values('student__id', 'student__first_name', 'student__last_name')