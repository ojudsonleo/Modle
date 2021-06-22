from django.shortcuts import render
from message.models import message
from portfolio.models import profile
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User

class register(CreateView):
    model = User
    template_name = "create_User.html"
    fields = "__all__"

class profile(ListView):
    model=profile
    template_name = "account-profile.html"

class Add_profile(CreateView):
    model=profile
    template_name = "add-profile.html"
    fields = "__all__"

class index(ListView):
    model=message
    template_name = "dashboard-1.html"

# def index(request):
#     return render(request, "dashboard-1.html")
def graphql(request):
    return render(request, "graphql.html")
def python(request):
    return render(request, "python.html")
def login(request):
    return render(request, "login.html")
def os(request):
    return render(request, "os.html")
def word_pratice(request):
    return render(request, "word_pratice.html")
