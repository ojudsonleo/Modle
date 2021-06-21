from django.db import models
from django.urls import reverse
# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse("profile")
