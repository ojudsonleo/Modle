from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . models import *
# Create your views here.
class HomeView(ListView):
    model = git
    template_name = "home.html"

class AddView(CreateView):
    model = git
    template_name="add_view.html"
    fields = "__all__"