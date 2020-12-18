from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, Register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout





# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect ('/login')
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your form is Submitted Successfully!')

    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        return redirect('/login')

    return render (request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        """ 
        check_user = Register.objects.filter(username=username).first()

        if check_user is None:
            return render (request, 'login.html')
        
        if check_user.password == password:
            return redirect ('/')
        else:
            return render (request, 'login.html')
        """

        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            return redirect('/')
        else:
            # the authentication system was unable to verify the username and password
            return redirect ('/login')

        

    return render (request, 'login.html')
    

def logoutUser(request):
    logout (request)
    return render (request, 'login.html')
    

