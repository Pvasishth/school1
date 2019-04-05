from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'student'

urlpatterns = [
  path('student/basic/',views.student_basic_info , name='basic_student')
]