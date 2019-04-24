from django.urls import path, include

from .import views

app_name = 'employes'


urlpatterns = [
  path('teacher/add',views.teacher, name='teacher_add'),


]