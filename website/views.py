from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):

    records = Record.objects.all

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
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
            #See record
            customer_record=Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record':customer_record})
    else:
          messages.error(request, "You must be logged in")
          return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.error(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)#checks wheter the user is filling out the form or just visiting
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added")
                return redirect('home')
                
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Login first to add record")
        return redirect('home') 

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



    

