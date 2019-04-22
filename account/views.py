from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required
from .models import  SchoolProfile , MediaUpload,Alert
from .forms import UserRegistrationForm,MediaUploadForm,SchoolProfileForm,Alert_form
from student.forms import StudentProfileForm

##########################################################################################################
from django.views.generic import CreateView
from .forms import StudentSignUpForm, TeacherSignUpForm, PrincipalSignUpForm
from django.contrib.auth import login
from .models import  User
from django.shortcuts import redirect

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class PrincipalSignUpView(CreateView):
    model = User
    form_class = PrincipalSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'principal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')
#############################################################################################################

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

    form = Alert_form(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        form = Alert.objects.create(title=title)

    return render(request, 'account/adminlte/create_alert.html',{'form': form})



def create_student(request):
    if request.method == 'POST':
        form =StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentProfileForm()
    return render(request, 'student/adminlte/create_student.html',{'s_form': form})


def feeds(request):
    alert = Alert.objects.all()
    return render(request, 'account/dashbord/feeds.html',{'alert':alert})


def add_class(request):
    return render(request, 'account/dashbord/add_class.html',{})