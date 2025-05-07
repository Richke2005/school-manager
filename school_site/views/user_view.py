from .base_view import BaseView
from ..services import UserService
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json


user_service = UserService()

class UserView(BaseView):
    def __init__(self, template_name: str = None):
        super().__init__(template_name, user_service)

    def create_user_view(self, request):
        if request.method == 'POST':
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST.dict()
                data.pop('csrfmiddlewaretoken', None)

            try:
                user_service.create_user(data)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                return JsonResponse({"error": str(e)}, status=400)

