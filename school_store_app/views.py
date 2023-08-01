from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect

from .forms import DetailCreationForm
from .models import Departments, Detail, Courses
from django.http import HttpResponse


def home(request):
    departments = Departments.objects.all()
    return render(request, 'home.html', {'departments': departments})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('school_store_app:form_page')
        else:
            messages.info(request, "Please check username & password")
            return redirect('school_store_app:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if username == '' or password == '' or cpassword == '':
            messages.info(request, "Please enter all fields")
            return redirect('school_store_app:register')
        else:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username is taken")
                    return redirect('school_store_app:register')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password)
                    user.save()
                    messages.info(request, "User Created")
                    return redirect('school_store_app:login')
            else:
                messages.info(request, "Passwords not matching")
                return redirect('school_store_app:register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def form_page(request):
    submitted = False
    form = DetailCreationForm()
    if request.method == 'POST':
        form = DetailCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form_page?submitted=True')
    else:
        form = DetailCreationForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'form.html', {'form': form, 'submitted': submitted})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
