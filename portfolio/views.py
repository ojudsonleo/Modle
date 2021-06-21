from . models import *
from django.views.generic import ListView, CreateView
# Create your views here.
class account_profile(ListView):
    model = profile
    template_name = "account-profile.html"

class add_profile(CreateView):
    model = profile
    template_name = "add-profile.html"
    fields = "__all__"