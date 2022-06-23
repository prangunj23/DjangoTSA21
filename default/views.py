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
from json import dumps
from .forms import RegisterUserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return HttpResponseRedirect(reverse("index"))

    else:
            form = RegisterUserForm()
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
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "default/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "default/login.html")

def logoutuser(request):
    logout(request)
    return render(request, "default/login.html", {
        "message": "Logged out."
    })
def user(request):
    if request.user.is_authenticated:
        if Event.objects.filter(username=request.user).exists():
            return render(request, "default/user.html", {
                "difficulty": element
            })
        else:
            return HttpResponseRedirect(reverse("loginevent"))

    else:
        return HttpResponseRedirect("login")

def loginevent(request):
    if request.user.is_authenticated:
        if Event.objects.filter(username=request.user).exists():
            newevent = Event.objects.filter(username_id=request.user.id)
            diff = newevent[0].difficulty
            novice = False
            intermediate = False
            advanced = False
            if element == "novice":
                novice = True
            elif element == "intermediate":
                intermediate = True
            else:
                advanced = True
            return render(request, "default/displayevent.html", {
                "difficulty": diff,
                "novice": novice,
                "intermediate": intermediate,
                "advanced": advanced,
            })
        else:
            return render(request, "default/eventlogin.html", {
                "difficulty": element
            })
    else:
        return HttpResponseRedirect(reverse("login"))
def event(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            useremail = request.POST["useremail"]
            lichessusername = request.POST["lichessusername"]
            userdifficulty = request.POST["userdifficulty"]
            event = Event(username=request.user, email=useremail, lichessusername=lichessusername, difficulty=userdifficulty)
            event.save()
            return HttpResponseRedirect(reverse("present"))
        else:
            return HttpResponseRedirect(reverse("loginevent"))
    else:
        return render(request, "default/login.html", {
        "message": "Please Log In"
        })

def updatediff(request):
    if request.user.is_authenticated:
        if Event.objects.filter(username=request.user).exists():
            userdifficulty = request.POST["userdifficulty"]
            lichessuser = request.POST["lichess"]
            entry = Event.objects.get(username=request.user)
            entry.difficulty = userdifficulty
            entry.lichessusername = lichessuser
            entry.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("event"))
    else:
        return HttpResponseRedirect(reverse("login"))

def present(request):
    if request.user.is_authenticated:
        if Event.objects.filter(username=request.user).exists():
            newevent = Event.objects.filter(username_id=request.user.id)
            novice = False
            intermediate = False
            advanced = False
            if newevent[0].difficulty == "novice":
                novice = True
            elif newevent[0].difficulty == "intermediate":
                intermediate = True
            else:
                advanced = True

            return render(request, "default/displayevent.html", {
                    "username": newevent[0].username.username,
                    "email": newevent[0].email,
                    "difficulty": newevent[0].difficulty,
                    "novice": novice,
                    "intermediate": intermediate,
                    "advanced": advanced
            })

def puzzles(request):
        return render(request, "default/puzzles.html")


def contact(request):
    if request.method == "POST":
        message_email = request.POST['message-email']
        message_name = request.POST['message-name']
        message = request.POST['message']
        

        send_mail(
            message_name,
            message,
            [message_email],
            "virchess123@gmail.com",
            fail_silently=False
        )

        return render(request, 'default/contact.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message': message,

        })

    else:
        return render(request, 'default/contact.html', {})

def lichess(request):
    if request.user.is_authenticated:
        if Event.objects.filter(username=request.user).exists():
            newevent = Event.objects.filter(username=request.user)
            lichessuser = newevent[0].lichessusername
            if not (lichessuser == ""):

                data = {
                    "username": lichessuser
                }
                username = dumps(data)
                return render(request, "default/lichess.html", {
                    "username": username
                })
            else:
                return HttpResponseRedirect(reverse('user'))
        else:
            return HttpResponseRedirect(reverse('loginevent'))

    else:
       return HttpResponseRedirect(reverse('login'))

def handler404(request, exception):
    return render(request, "default/404.html", status=404)
