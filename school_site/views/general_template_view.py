from .base_view import BaseView


class GeneralTemplateView(BaseView):
    def __init__(self, template_name: str = None, service = None):
        super().__init__(template_name, service)

