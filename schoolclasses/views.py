from django.shortcuts import render , redirect
from .models import *
from account.forms import Class_Add_form
from.forms import section_add_form
# Create your views here.





def add_class(request):
    if request.method == 'POST':
        form =Class_Add_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('account:schoolclass:class_list')
    else:
        form = Class_Add_form()
    return render(request, 'schoolclasses/add_class.html', {'s_form':form})


def view_class(request):
    clas_list = Class.objects.all()
    return render(request, 'schoolclasses/class_list.html', {'list':clas_list})



def add_section(request):
    if request.method == 'POST':
        form = section_add_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('account:schoolclass:section_view')
    else:
        form = section_add_form()
    return render(request,'schoolclasses/add_section.html',{'form':form})


def list_section(request):
    section_list = Section.objects.all()
    return render(request,'schoolclasses/view_section.html',{'list':section_list})


