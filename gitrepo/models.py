from django.db import models
from django.urls import reverse
# Create your models here.
class git(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("home")