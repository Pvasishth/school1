from django.shortcuts import render,HttpResponse
from .forms import *
# Create your views here.

def teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Teacher Added')
    else:
        form = TeacherForm()
    return render(request,'account/adminlte/teacher_add.html',{'form':form})

