from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import Teacher
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView
from django.shortcuts import render,get_object_or_404
from employes.forms import LoginForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator









class LoginView(DefaultLoginView): # FormView
    authentication_form = LoginForm
    template_name = 'employes/login.html'
    success_url = 'account:dashboard'


class LogoutView(DefaultLogoutView):
    success_url = 'teacher_add'
from .models import Teacher, Homework

# Create your views here.




def teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('employes:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'employes/dashbord/teacher_add.html', {'form':form})


def teacher_list_view(request):
    teacher_list = Teacher.objects.all()
    return render(request,'employes/dashbord/teacher_list.html',{'tach_list':teacher_list})


def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employes:homework_list')
    else:
        form = HomeworkForm()
    return render(request, 'employes/dashbord/homework_add.html', {'form':form})

def homework_list_view(request):
    homework_list = Homework.objects.all()
    return render(request,'employes/dashbord/homework_list.html',{'home_list':homework_list})

def homework_delete(request, id):
    obj = get_object_or_404(Homework, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'object': obj
    }
    return render(request, 'employes/dashbord/confirm_delete_homework.html', context)


# def homework_detail_view(request, id):
#     homework_detail = Homework.objects.get(id=id)
#     return render(request, 'employes/dashbord/homework_detail.html', {'detail_view': homework_detail})


def assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employes:assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'employes/dashbord/assignment_add.html', {'a_form':form})


def assignment_list_view(request):
    assignment_list = Assignment.objects.all()
    return render(request,'employes/dashbord/assignment_list.html',{'assign_list':assignment_list})


def gallery(request):
    if request.method =='POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponse('SUBMITTTTTTTTTTTTT')
            return redirect('employes:gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'employes/dashbord/gallery_add.html', {'gallery_form':form})

def gallery_list_view(request):
    gallery_list = Gallery.objects.all()
    return render(request,'employes/dashbord/gallery_list.html' ,{'gallery_list':gallery_list})


#
# def index(request):
#   listings = Listing.objects.order_by('-list_date')
#
#   # paginator = Paginator(listings, 6)
#   # page = request.GET.get('page')
#   # paged_listings = paginator.get_page(page)
#
#   context = {
#     'listings': listings
#   }
#
#   return render(request, 'gallery/photos.html', {'list_form':listings})
#
#
#
# def listing(request, listing_id):
#   listing = get_object_or_404(Listing, pk=listing_id)
#
#   context = {
#     'listing': listing
#   }
#
#   return render(request, 'gallery/photo.html', context)
