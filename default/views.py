from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        
            form = UserCreationForm()
    return render(request, "default/register.html", {'form': form})

def index(request):
    return render(request, "default/index.html")
 

    
def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "default/index.html", {})
            
        else:
            return render(request, "default/index.html", {
                "message": "Invalid credentials."
            })
    return render(request, "default/login.html")

def logoutuser(request):
    logout(request)
    return render(request, "default/login.html", {
        "message": "Logged out."
    })
def user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "default/user.html")

