from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import GeneralTemplateView, ClassView, UserView, DisciplineView

general_view = GeneralTemplateView()
classes_view = ClassView("user/classes/classes.html")
disciplines_view = DisciplineView("user/disciplines/disciplines.html")
user_view = UserView("manager/users_management/users.html")

urlpatterns = [
    path('', lambda request: general_view.load_template_view(request, template_name='public/index.html', require_login=False), name='landing_page'),
    path('auth/login/', LoginView.as_view(template_name='auth/login/login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/forgot_password/', lambda request: general_view.load_template_view(request, template_name="auth/forgot_password/forgot_password.html", require_login=False), name='forgot_password'),
    path('home/', lambda request: general_view.load_template_view(request, template_name="user/home.html", require_login=True), name='home'),
    path('management/user/', lambda request: user_view.load_data_view(request), name="user_management"),
    path('management/user/create/', lambda request: user_view.create_user_view(request), name="user_management_create"),
    path('management/user/<int:id>', lambda request, id: user_view.delete_view(request, id), name="delete_user"),
    path('disciplines/', lambda request: disciplines_view.load_my_disciplines_view(request), name="disciplines"),
    path('disciplines/<int:id>/detail', lambda request, id: disciplines_view.load_discipline_detail_view(request, id), name="discipline_detail"),
    path('classes/', lambda request: classes_view.load_my_classes_view(request), name="classes"),
    path('classes/<int:id>/students', lambda request, id: classes_view.load_class_students_view(request, id), name="class_students"),
    path('students/', lambda request: general_view.load_template_view(request, template_name="user/students/students.html", require_login=True), name="students"),
]