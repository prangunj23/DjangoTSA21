from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, element, DIFFICULTY
import datetime
from django.http import request
from django.core.mail import send_mail
from django.conf import settings


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

def about(request):
    return render(request, "default/about.html")

def sources(request):
    return render(request, "default/sources.html")

def contact(request):
    return render(request, "default/contact.html")

def press(request):
    return render(request, "default/press.html")

def es(request):
    return render(request, "default/es.html")

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

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
    newevent = Event.objects.filter(username=request.user)
    return render(request, "default/user.html", {
        "username": newevent[0].username.username,
        "email": newevent[0].email,
        "difficulty": newevent[0].difficulty
    })

def loginevent(request):
    return render(request, "default/eventlogin.html", {
        "difficulty": element
    })
def event(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            
            useremail = request.POST["useremail"]
            at = '@'
            if not at in useremail:
                return render(request, "default/eventlogin.html", {
                    "difficulty": element,
                    "message": "Please input a correct email"
                })

            userdifficulty = request.POST["userdifficulty"]
            event = Event(username=request.user, email=useremail, difficulty=userdifficulty)
            event.save()
            if Event.objects.filter(username=request.user).exists():
                existing = True
            else:
                existing = False

            newevent = Event.objects.filter(username_id=request.user.id)
            return render(request, "default/displayevent.html", {
                "username": newevent[0].username.username,
                "email": newevent[0].email,
                "difficulty": newevent[0].difficulty,
                "existing": existing
            })
        else:
            return HttpResponseRedirect(reverse("loginevent"))
    else:
        return render(request, "default/login.html", {
        "message": "Please Log In"
        })

def updatediff(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userdifficulty = request.POST["useremail"]
            entry = Event.objects.get(username=request.user.username)
            entry.difficulty = userdifficulty
            entry.save()
            return HttpResponseRedirect(reverse("event"))


def puzzles(request):
        return render(request, "default/puzzles.html")


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        msg_mail = str(message) + "\n\nFrom:" + str(message_name)

        send_mail(
            str(message_email),
            msg_mail,
            message_email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        return render(request, 'default/contact.html', {'message_name': message_name,
                                              'message_email': message_email,
                                              'message': message})
    else:
        return render(request, 'default/contact.html', {})
