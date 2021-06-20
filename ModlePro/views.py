from django.shortcuts import render
from message.models import message
from django.views.generic import ListView

class index(ListView):
    model=message
    template_name = "dashboard-1.html"

# def index(request):
#     return render(request, "dashboard-1.html")
def graphql(request):
    return render(request, "graphql.html")
def python(request):
    return render(request, "python.html")
def register(request):
    return render(request, "register.html")
def login(request):
    return render(request, "login.html")
def os(request):
    return render(request, "os.html")
def word_pratice(request):
    return render(request, "word_pratice.html")
