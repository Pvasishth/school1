from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import Teacher
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from account.forms import LoginForm







class LoginView(DefaultLoginView): # FormView
    authentication_form = LoginForm
    template_name = 'employes/login.html'
    success_url = '/'


class LogoutView(DefaultLogoutView):
    success_url = '/'

def teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('account:employes:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'employes/dashbord/teacher_add.html', {'form':form})


def teacher_list_view(request):
    teacher_list = Teacher.objects.all()
    return render(request,'employes/dashbord/teacher_list.html',{'tach_list':teacher_list})