from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views

app_name = 'employes'


urlpatterns = [
  path('teacher/add',views.teacher, name='teacher_add'),
  path('teacher/list', views.teacher_list_view, name='teacher_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)