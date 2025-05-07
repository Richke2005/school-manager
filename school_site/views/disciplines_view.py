from .base_view import BaseView
from ..services import DisciplineService, AbsenceService
from django.shortcuts import render
from django.http import JsonResponse


discipline_service = DisciplineService()
absence_service = AbsenceService()

class DisciplineView(BaseView):
    def __init__(self, template_name: str = None):
        super().__init__(template_name, discipline_service)

    def load_my_disciplines_view(self, request):
        if request.method == 'GET':
            user = request.user
            try:
                disciplines = discipline_service.get_my_disciplines(user)
                return render(request, self.template_name, {"data": disciplines})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
            
    def load_discipline_detail_view(self, request, id):
        if request.method == 'GET':
            user = request.user
            try:
                discipline = discipline_service.get_discipline_by_id(id, user)
                return render(request, "user/disciplines/discipline_detail.html", {"data": discipline})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
    
    def load_discipline_presence_view(self, request, id):
        if request.method == 'GET':
            user = request.user
            try:
                absences = absence_service.get_absences_by_discipline_id(id)
                print(absences)
                return render(request, "user/disciplines/discipline_presence.html", {"data": absences})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)

