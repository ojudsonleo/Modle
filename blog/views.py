from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView,DeleteView
from .models import *
# def Blog(request):
#     return render(request, "home.asp")

class Blog(ListView):
    model = Post
    template_name = "home.asp"

class ArticleDetailView(DeleteView):
    model = Post
    template_name = "article_detail.asp"