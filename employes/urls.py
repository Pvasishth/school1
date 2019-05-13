from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import auth_login
from .import views
from .forms import LoginForm

app_name = 'employes'


urlpatterns = [
  path('teacher/',views.dashbord,name='dashbord'),
  path('teacher/feeds/',views.feeds,name='employes_feeds'),
  path('teacher/alert/',views.create_alert,name='create_alert'),
  path('teacher/alert/list/',views.alert_list,name='alert_list'),
  path('teacher/add',views.teacher, name='teacher_add'),
  path('teacher/add/profile',views.Teacher_Profile,name='teacher_profile_add'),
  path('teacher/profile/<int:id>/',views.teacher_profile_detail,name='teacher_profile_detail'),
  path('teacher/list', views.teacher_list_view, name='teacher_list'),
  path('homework/list', views.homework_list_view, name='homework_list'),
  path('assignment/list', views.assignment_list_view, name='assignment_list'),
  # path('homework/delete/<int:id>', views.homework_delete, name = 'confirm_delete_homework'),
  path('teacher/login/',views.LoginView.as_view(),name='login'),
  path('teacher/logout',views.LogoutView.as_view(),name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)