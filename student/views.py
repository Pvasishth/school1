from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import *
from .forms import *
from.models import *
# Create your views here.
@login_required
def student_basic_info(request):
    if request.method == 'POST':
        basic_student = StudentProfileForm(instance= request.user.studentprofile,
                                            data = request.POST)
        if basic_student.is_valid():
            basic_student = basic_student.save(commit=False)
            basic_student.save()
    else:
        basic_student = StudentProfileForm(instance= request.user.studentprofile)
    return render(request,'profile.html',{'basic_student':basic_student})


def index(request):
    return render(request,'student/adminlte/index.html',{})


def feed(request):
    alert = Alert.objects.all()
    return render(request, 'student/dashbord/student_feed.html',{'alert':alert})


def create_student(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('account:student:student_list')
    else:
        form = StudentProfileForm()
    return render(request, 'student/adminlte/create_student.html',{'s_form': form})



def student_list_view(request):
    student_list = StudentProfile.objects.all()
    return render(request,'student/dashbord/student_list.html',{'std_info':student_list})

def student_details_view(request):
    std_detail = StudentProfile.objects.get(id=id)
    return render(request,'student/dashbord/student_detail.html',{'std_detail':std_detail})