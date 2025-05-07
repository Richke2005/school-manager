import json
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.http import JsonResponse

class BaseView:
    def __init__(self, template_name: str, service):
        self.template_name = template_name
        self.service = service

    def _set_required_decorator(self, require_login: bool):
        """Set the appropriate required decorator based on the login requirement."""
        return login_required if require_login else lambda x: x

    def load_template_view(self, request, template_name: str = '', require_login: bool = True):
        """Render the given template with an optional login requirement."""
        decorator = self._set_required_decorator(require_login)
        request = decorator(lambda req: req)(request)  # Apply the decorator dynamically
        return render(request, template_name)

    def load_data_view(self, request, require_login: bool = True):
        decorator = self._set_required_decorator(require_login)
        request = decorator(lambda req: req)(request)
        return render(request, self.template_name, {'data': self.service.get_all()})

    def change_template_to(self, request, template_name: str = None, require_login: bool = True):
        decorator = self._set_required_decorator(require_login)
        request = decorator(lambda req: req)(request)
        return render(request, template_name, {'data': self.service.get_all()})

    @method_decorator(login_required)
    def get_by_pk_view(self, request, id):
        if request.method == 'GET':
            try:
                return JsonResponse(self.service.get_by_pk(id))
            except ValueError as e:
                raise Http404(f"{e}")

    @method_decorator(login_required)
    def create_view(self, request):
        if request.method == 'POST':
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST.dict()
                data.pop('csrfmiddlewaretoken', None)

            try:
                self.service.create(data)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                return JsonResponse({"error": str(e)}, status=400)

    @method_decorator(login_required)
    def update_view(self, request, id):
        if request.method == 'POST':
            data = request.POST
            return JsonResponse(self.service.update(id, data))

    @method_decorator(login_required)
    def delete_view(self, request, id):
        if request.method == 'DELETE':
            return JsonResponse(self.service.delete(id))
        else:
            return Http404("Invalid request method")

    @method_decorator(login_required)
    def ajax_create_view(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            return JsonResponse(self.service.create(data))

    @method_decorator(login_required)
    def ajax_update_view(self, request, id):
        if request.method == 'PUT':
            data = json.loads(request.body)
            return JsonResponse(self.service.update(id, data))