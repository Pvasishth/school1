from django.shortcuts import render,redirect
from account.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.decorators import student_required
from django.contrib.auth.views import LoginView,LogoutView
from student.forms import *
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


class Login(LoginView):
    authentication_form = LoginForm
    template_name = 'student/login.html'
    success_url = 'student:dashboard'

class Logout(LogoutView):
    success_url = '/'


@login_required
@student_required
def feed(request):
    alert = Alert.objects.all()
    # homework = Homework.objects.all()
    return render(request, 'student/dashbord/student_feed.html', {'alert':alert})


def user_student(request):
    if request.method == 'POST':
        student_form=RegisterForm(request.POST)
        if student_form.is_valid():
            new_user =student_form.save(commit=False)
            new_user.set_password('password')
            new_user.is_student=True
            new_user.save()
            return redirect('student:student_profile')
    else:
        student_form =RegisterForm()
    return render(request,'student/create_student.html',{'student_form':student_form})


def student_profile(request):
    if request.method == 'POST':
        profile_form = StudentProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save(commit=False)
            user = User.objects.all().last()
            userid = user.id
            profile_form.user = userid
            profile_form.save()
        return redirect('account:create_alert')
    else:
        profile_form = StudentProfileForm(request.POST)
    return render(request, 'student/student_profile_add.html', {'pro_user': profile_form})



def student_list_view(request):
    student_list = StudentProfile.objects.all()
    return render(request,'student/dashbord/student_list.html',{'std_info':student_list})

def student_details_view(request, id):
    std_detail = StudentProfile.objects.get(id=id)
    return render(request,'student/student_profile.html',{'std_detail':std_detail})

