from .service import Service
from ..models import Discipline, User_Discipline

class DisciplineService(Service):
    def __init__(self):
        super().__init__(Discipline)

    def get_my_disciplines(self, user):
        """
        Get all disciplines for the given user.
        """
        
        user_disciplinas = self.model.objects.filter(user_discipline__user=user).distinct()
        return user_disciplinas
    
    def get_discipline_by_id(self, id, user):
        """
        Get a discipline by its ID for the given user.
        """
        try:
            discipline = self.model.objects.get(id=id)
            return discipline
        except Discipline.DoesNotExist:
            raise ValueError("Discipline not found or you do not have access to it.")
    