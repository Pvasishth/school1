from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import Teacher
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render
from account.forms import RegisterForm
from employes.forms import LoginForm
from django.contrib.auth import authenticate, login
from account.models import User ,Alert
from account.forms import Alert_form
from account.decorators import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect


class LoginView(DefaultLoginView): # FormView
    authentication_form = LoginForm
    template_name = 'employes/login.html'
    success_url = 'employes'




# def user_login(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = authenticate(username=username, password=password)
#             if user.is_active and user.is_teacher:
#                 login(request,user)
#                 return HttpResponse('done')
#             el
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password']
#                                 )
#             if user is not None:
#                 if user.is_active and user.is_teacher:
#                     login(request, user)
#                     print(cd['username'], cd['password'])
#                     return HttpResponse('Authenticate Successfully')
#             else:
#                 return HttpResponse('not teacher')
#         else:
#             return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request,'employes/login.html',{'form':form})

class LogoutView(DefaultLogoutView):
    success_url = 'teacher_add'

def dashbord(request):
    return render(request,'employes/adminlte/index.html')
@teacher_required
def create_alert(request):
    if request.method =='POST':
        form = Alert_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = Alert_form()
    return render(request,'employes/dashbord/create_alert.html',{'form':form})

@teacher_required
def alert_list(request):
    list = Alert.objects.all()
    render(request,'employes/dashbord/list_alert.html',{'alert_list':list})


@teacher_required
def feeds(request):
    feeds = Alert.objects.all()
    return render(request,'employes/dashbord/teacher_feeds.html',{'feeds':feeds})




def teacher(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password('password')
            new_user.is_teacher = True
            new_user.save()
            return redirect('employes:teacher_profile_add')
    else:
        user_form = RegisterForm()
    return render(request,'employes/dashbord/teacher_add.html',{'user_form':user_form})



def Teacher_Profile(request):
    if request.method == 'POST':
        teacher_form = Teacher_Profile_form(request.POST or None)
        if teacher_form.is_valid():
            teacher_form.save(commit=False)
            # TODO: user is not going without select in profile fix it as soon as possible
            user = User.objects.get(teacher_form.auto_id)
            print(user)
            teacher_form.user =user
            teacher_form.save()
            return redirect('account:create_alert')
    else:
        teacher_form = Teacher_Profile_form()
    return render(request,'employes/dashbord/teacher_profile_add.html',{'teacher_form':teacher_form})



def teacher_list_view(request):
    teacher_list = Teacher.objects.all()
    return render(request,'employes/dashbord/teacher_list.html',{'tach_list':teacher_list})



