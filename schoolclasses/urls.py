from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'schoolclass'

urlpatterns = [
  path('class/view',views.view_class, name='class_list'),
  path('class/add',views.add_class, name='clas_add'),
  path('section/add',views.add_section,name='section_add'),
  path('section/view', views.list_section, name='section_view'),

]