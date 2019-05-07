from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from django.conf.urls.static import static
from django.conf import settings

from schoolclasses import urls
app_name = 'student'

urlpatterns = [
  path('',views.index,name='dashboard'),
  path('add', views.create_student, name='create_student'),
  path('login',views.Login.as_view(),name='student_login'),
  path('logout', views.LogoutView.as_view(), name='logout'),
  path('view/<int:pk>',views.student_details_view,name='student_detail'),
  path('list/', views.student_list_view, name='student_list'),
  path('basic/',views.student_basic_info , name='basic_student'),
  path('feeds/', views.feed, name='feeds'),
]