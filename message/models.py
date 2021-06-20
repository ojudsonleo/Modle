from django.db import models
# Create your models here.
class message(models.Model):
    message = models.CharField(max_length=200, blank=True)
    alert = models.CharField(max_length=200, default="message whas sended", blank=True)
    date = models.DateTimeField(auto_now_add=True)