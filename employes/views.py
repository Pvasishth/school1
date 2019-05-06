from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import Teacher
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from employes.forms import LoginForm








class LoginView(DefaultLoginView): # FormView
    authentication_form = LoginForm
    template_name = 'employes/login.html'
    success_url = 'account:dashboard'


class LogoutView(DefaultLogoutView):
    success_url = 'teacher_add'
from .models import Teacher, Homework

# Create your views here.

# def homework_delete(request, id):
#     obj = get_object_or_404(Homework, id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, 'employes/dashbord/confirm_delete_homework.html', context)



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


def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account:employes:homework_list')
    else:
        form = HomeworkForm()
    return render(request, 'employes/dashbord/homework_add.html', {'form':form})

def homework_list_view(request):
    homework_list = Homework.objects.all()
    return render(request,'employes/dashbord/homework_list.html',{'home_list':homework_list})

# def homework_detail_view(request, id):
#     homework_detail = Homework.objects.get(pk=id)
#     return render(request, 'employes/dashboard/homework_detail.html', {'detail_view': detail_view})


# std_detail = StudentProfile.objects.get(pk=id)
def assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('account:employes:assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'employes/dashbord/assignment_add.html', {'a_form':form})


def assignment_list_view(request):
    assignment_list = Assignment.objects.all()
    return render(request,'employes/dashbord/assignment_list.html',{'assign_list':assignment_list})