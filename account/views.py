from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse


from django.shortcuts import render , HttpResponse ,reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from .forms import *
from .decorators import *
from .models import *
from employes.forms import *
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from .forms import LoginForm



def dashboard(request):
    return render(request, 'account/adminlte/index.html')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST, files=request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password('password')
            new_user.save()
            return HttpResponse('Done')
    else:
        user_form = RegisterForm()
    return render(request,'account/dashbord/form.html',{'user_form':user_form})


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

from django.core.mail import send_mail
def create_alert(request):
    sent = False
    if request.method == 'POST':
            form = Alert_form(data=request.POST, files=request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                print(cd['mail_check'])
                post_url = request.build_absolute_uri()
                subject = f"Alert {cd['title']} {post_url}"
                print(subject)
                message = f"{cd['message']}"
                if cd['mail_check']:
                    print(form.cleaned_data)
                    send_mail(subject, message, 'gupta1997abhishek96@gmail.com', ['gupta1997abhishek@gmail.com','paras.vasisth@gmail.com'],fail_silently=False)
                    sent = True
                    form.save()
                else:
                    form.save()
            else:
                 return HttpResponse('invalid')
            return HttpResponse('done')
    else:
       form = Alert_form()
    return render(request, 'account/adminlte/create_alert.html',{'form': form,
                                                                 'sent':sent})


def alert_list(request):
    list = Alert.objects.all()
    return render(request,'account/dashbord/alert_list.html',{'alert':list})


def feeds(request):
    alert = Alert.objects.all()
    return render(request, 'account/dashbord/feeds.html',{'alert':alert})


def add_class(request):
    return render(request, 'account/dashbord/formadd_class.html',{})

from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render

from .forms import LoginForm

from django.core.mail import send_mail


class LoginView(DefaultLoginView):
    authentication_form = LoginForm
    template_name = 'account/login.html'
    success_url = 'account:dashboard'




class LogoutView(DefaultLogoutView):
    success_url = '/'


def registerform(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('account:student:student_list')
    else:
        form = RegisterForm()
    return render(request, 'account/dashbord/form.html',{'s_form':form})

def academic_calender(request):
    if request.method == 'POST':
        form = AcademicCalenderForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse('Done')
    else:
        form = AcademicCalenderForm()
    return render(request,'account/adminlte/calender.html',{'form':form})

def time_table(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Done')
    else:
        form = TimeTableForm()
    return render(request,'account/adminlte/time_table.html',{'form':form})

def syllabus(request):
    if request.method == 'POST':
        form = SyllabusForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SyllabusForm()
    return render(request,'account/adminlte/syllabus.html',{'form':form})

# def _send(request):
#         try:
#             # twilio version 6
#             from twilio.rest import Client
#         except ImportError:
#             try:
#                 # twillio version < 6
#                 from twilio.rest import TwilioRestClient as Client
#             except ImportError:
#                 raise Exception('Twilio is required for sending a TwilioTextNotification.')
#
#         try:
#             account_sid = settings.TWILIO_ACCOUNT_SID
#             auth_token = settings.TWILIO_AUTH_TOKEN
#         except AttributeError:
#             raise Exception(
#                 'TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN settings are required for sending a TwilioTextNotification'
#             )
#
#         client = Client(account_sid, auth_token)
#
#         client.messages.create(
#             body='HELLO',
#             to='+919971271794',
#             from_='+17209243923'
#         )






