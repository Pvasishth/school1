from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import  SchoolProfile , MediaUpload
from .forms import UserRegistrationForm,MediaUploadForm,SchoolProfileForm
from student.forms import StudentProfileForm

def dashboard(request):
    return render(request, 'account/adminlte/index.html')

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            # Create a new user object but avoid saving yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password('password')
            #save the user  objects
            new_user.save()
            SchoolProfile.objects.create(principal=new_user)


            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()


    return render(request,'account/register.html',{'user_form':user_form})



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
            alert_form = Alert_form(request.POST)
            if alert_form.is_valid():
                alert_form = alert_form.save()

    else:
        alert_form = Alert_form()
    return render(request, 'account/adminlte/create_alert.html',{'form': alert_form})



def create_student(request):
    if request.method == 'POST':
        form =StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentProfileForm()
    return render(request, 'student/adminlte/create_student.html',{'s_form': form})