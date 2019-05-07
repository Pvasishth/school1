from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name = 'account'

urlpatterns = [
  

  path('', views.dashboard , name='dashboard'),
  path('alert/create/', views.create_alert,name='create_alert'),
  path('register/form/',views.register,name='RegisterForm'),
  path('login/',views.LoginView.as_view(),name='login'),
  path('logout',views.LogoutView.as_view(),name='logout'),
  # path('login/',auth_views.LoginView.as_view() , name='login'),
  # path('logout/',auth_views.LogoutView.as_view() , name='logged_out'),
  # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  # path('register/',views.register, name='register'),
  # path('account/profile_edit/',views.basic_info ,name = 'edit_profile'),
  # path('account/media_upload/',views.edit_media , name = 'edit_media'),

  # path('account/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
  # path('account/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
  # path('account/signup/principal/', views.PrincipalSignUpView.as_view(), name='principal_signup'),
  #

  #All Student url
  path('feeds/', views.feeds, name='feeds'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)