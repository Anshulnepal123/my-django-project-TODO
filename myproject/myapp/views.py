from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from myapp.models import Todo


# Create your views here.
def main(request):
    return render(request,'login.html')
def home(request):
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            desc = request.POST.get('des')
            date = request.POST.get('date')
            todo = Todo(title=title, description=desc, due_date=date)
            todo.save()
    except:
        return HttpResponse("Please fill the form")
    doit = Todo.objects.all()
    
    return render(request, 'home.html', {'doit': doit})
def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['pass']
            #check for errors 
            #create user
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('home')
    except:
        return('username is already choosen')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['pass']
        user = authenticate(username=username, password=pw)

        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            messages.success(request, 'Successfully logged in')
            return redirect('home')
        else:
            print("Invalid credentials")
            messages.error(request, 'Invalid credentials')
            return redirect('/')
    return render(request,'login.html')

def delete(request,pk):
    dele = Todo.objects.get(id=pk)
    dele.delete()
    return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('/')
    
