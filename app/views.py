from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from . models import *
from . forms import *
# Create your views here.
class project_home(ListView):
    model = project
    template_name = "projects.html"

class CreateProject(CreateView):
    form_class = CreateForm
    model = project
    template_name = "add_project.html"


class Info(DeleteView):
    model = project
    template_name = "detail_project.html"

class DeleteProject(DeleteView):
    model = project
    template_name = "delete_project.html"
    success_url = reverse_lazy('project_list')