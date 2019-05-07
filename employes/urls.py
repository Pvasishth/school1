from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views

app_name = 'employes'


urlpatterns = [
  path('teacher/add',views.teacher, name='add_teacher'),
  path('homework/add', views.homework, name= 'homework_add'),
  path('assignment/add', views.assignment, name = 'assignment_add'),
  path('teacher/list', views.teacher_list_view, name='teacher_list'),
  path('homework/list', views.homework_list_view, name='homework_list'),
  path('assignment/list', views.assignment_list_view, name='assignment_list'),
  # path('homework/delete/<int:id>', views.homework_delete, name = 'confirm_delete_homework'),
  path('teacher/login/',views.LoginView.as_view(),name='login'),
  path('teacher/logout',views.LogoutView.as_view(),name='logout'),
]