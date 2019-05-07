from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views

app_name = 'employes'


urlpatterns = [
  path('teacher/add',views.teacher, name='teacher_add'),
  path('homework/add', views.homework, name= 'homework_add'),
  path('assignment/add', views.assignment, name = 'assignment_add'),
  path('teacher/list', views.teacher_list_view, name='teacher_list'),
  path('homework/list', views.homework_list_view, name='homework_list'),
  path('assignment/list', views.assignment_list_view, name='assignment_list'),
  path('listings/add', views.listings, name = 'listings_add'),
  path('listings/list', views.listings_list_view, name='listings_list'),
  # path('gallery', views.index, name='photos'),
  # path('gallery/<int:listing_id>', views.listing, name='photo'),
  # path('homework/delete/<int:id>', views.homework_delete, name = 'confirm_delete_homework'),
  # path('principal/login',name='login')
  path('teacher/login/',views.LoginView.as_view(),name='login'),
  path('teacher/logout',views.LogoutView.as_view(),name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)