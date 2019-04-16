from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import  SchoolProfile
from .forms import StudentProfileForm
from account.models import Alert

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