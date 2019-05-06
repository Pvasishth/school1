from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *
from django.shortcuts import redirect


@login_required
@teacher_required
def dashboard(request):
    return render(request, 'account/adminlte/index.html')

def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password('password')
            #save the user  objects
            new_user.save()
            SchoolProfile.objects.create(principal=new_user)
            return HttpResponse('Done')
                # render(request,'student/create_student.html',{'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request,'account/dashbord/form.html',{'user_form':user_form})


# def login(request):
#     return HttpResponse('hello from login')
#




def edit_media(request):
    if request.method == 'POST':

        input_form = MediaUploadForm(instance = request.user.MediaUpload,
                                    data=request.POST)
        if input_form.is_valid():
            input_form = input_form.save(commit = False)

            input_form.save()
    else:
        input_form = MediaUploadForm(instance = request.user.MediaUpload)

    return render(request,'account/upload_media.html',{'input_form':input_form})

@login_required
def basic_info(request):
    if request.method == 'POST':
        basic = SchoolProfileForm(instance = request.user.schoolprofile,
                                data = request.POST)
        if basic.is_valid():
            basic = basic.save(commit = False)
            basic.save()
    else:
        basic = SchoolProfileForm(instance = request.user.schoolprofile)
    return render(request,'account/profile.html',{'basic':basic})


def create_alert(request):
    if request.method == 'POST':
            form = Alert_form(request.POST)
            print(form)
            if form.is_valid():
                form.save()
            return HttpResponse('submited')
    else:
        form = Alert_form()
    return render(request, 'account/adminlte/create_alert.html',{'form': form})




def feeds(request):
    alert = Alert.objects.all()
    return render(request, 'account/dashbord/feeds.html',{'alert':alert})


def add_class(request):
    return render(request, 'account/dashbord/formadd_class.html',{})

from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from .forms import LoginForm

# form= self.form_class(request.POST)
# if form.is_valid():
#     user=form.save(commit=False)
#
#     username = form.cleaned_data['email']
#     password=form.cleaned_data['password']
#     user.set_password(password)
#     user.save()
#
#     user = authenticate(username=username,password=password)
#     if user is not None:
#         if user.is_principal:
#             login(request, user)
#             return redirect('account:dashboard')
#
#
#

class LoginView(DefaultLoginView):
    authentication_form = LoginForm
    template_name = 'account/login.html'
    success_url = 'account:dashboard'


class LogoutView(DefaultLogoutView):
    success_url = '/'


def registerform(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('account:student:student_list')
    else:
        form = RegisterForm()
    return render(request, 'account/dashbord/form.html',{'s_form':form})