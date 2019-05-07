from django.shortcuts import render,redirect
from account.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.decorators import student_required
from django.contrib.auth.views import LoginView,LogoutView
from student.forms import *
from.models import *
from employes.models import Homework
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
@login_required
@student_required
def index(request):
    return render(request,'student/adminlte/index.html',{})


class Login(LoginView):
    authentication_form = LoginForm
    template_name = 'student/login.html'


    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'student'
    #     return super().get_context_data(**kwargs)
    #
    # def form_valid(self, form):
    #     return redirect('student:dashboard')

class Logout(LogoutView):
    success_url = '/'


@login_required
@student_required
def feed(request):
    alert = Alert.objects.all()
    # homework = Homework.objects.all()
    return render(request, 'student/dashbord/student_feed.html', {'alert':alert})

@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            user =StudentProfile.objects.create(user=form)
        return redirect('account:student:student_list',{'user':user})
    else:
        form = StudentProfileForm()
    return render(request, 'student/create_student.html', {'s_form': form})



def student_list_view(request):
    student_list = StudentProfile.objects.all()
    return render(request,'student/dashbord/student_list.html',{'std_info':student_list})

def student_details_view(request, id):
    std_detail = StudentProfile.objects.get(pk=id)
    return render(request,'student/student_profile.html',{'std_detail':std_detail})

