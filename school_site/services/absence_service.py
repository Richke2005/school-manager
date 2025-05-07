from .service import Service
from ..models import Absence

class AbsenceService(Service):
    def __init__(self):
        super().__init__(Absence)

    def get_absences_by_discipline_id(self, discipline_id):
        """
        Get absences by discipline ID.
        """
        return self.model.objects.filter(discipline_id=discipline_id).values(
            'id',
            'student__id',
            'student__first_name', 
            'student__last_name',
            'justification__submission_date',
            'absence_date', 
            'is_present',
            'absence_status').order_by('absence_date')
