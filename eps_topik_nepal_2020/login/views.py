from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.session.has_key('username'):
        return redirect('/book')
    else:

        return render(request, 'login/index.html')


def logout(request):
    try:
        del request.session['username']
        auth.logout(request)
    except:
        pass
    
    return redirect('/login')


def signin(request):
    if request.method == "POST":
        userName = request.POST['username']
        passWord = request.POST['password']
        user = auth.authenticate(username=userName, password=passWord)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = userName
            
            return redirect('/book')

        else:
            return redirect('/login')


def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                       password=password)
        user.save()
        return redirect('/login')
    else:
        return render(request, '/login/index.html')
