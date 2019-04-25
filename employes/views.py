from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import Teacher
# Create your views here.

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