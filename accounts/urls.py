from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", views.user_list, name="user_list"),
    path("students/", views.student_list, name="student_list"),
    path("students/add-fbv/", views.add_student, name="add_student"),
    path("students/add-cbv/", views.StudentCreateCBV.as_view(), name="add_student_cbv"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("students/delete/<int:pk>/", views.delete_student, name="delete_student"),
]