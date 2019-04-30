from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.conf.urls.static import static
from django.conf import settings

from schoolclasses import urls
app_name = 'student'

urlpatterns = [
  path('',views.index,name='home'),
  path('add', views.create_student, name='create_student'),
  path('view/<int:pk>',views.student_details_view,name='student_detail'),
  path('list/', views.student_list_view, name='student_list'),
  path('basic/',views.student_basic_info , name='basic_student'),
  path('feeds/', views.feed, name='feeds'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)