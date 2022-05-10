from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255,default=None)
    description = models.TextField(max_length=250 ,default=None)
    pic = models.ImageField(upload_to='images/',height_field=None, width_field=None)
    # date_posted =  models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title