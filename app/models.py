from django.db import models

from django.urls import reverse
# Create your models here.
class project(models.Model):
    project_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    langvage = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("project_list")