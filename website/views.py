from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #checks if user is login in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authentification
        user = authenticate(request, username=username, password=password)

        #check fills
        if user is not None:
            login(request, user)
            messages.success(request, "You are loged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Try again")
            return redirect('home')
    else: 
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})