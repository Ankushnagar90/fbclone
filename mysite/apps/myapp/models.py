from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import UserManager


class Post(models.Model):
    
    title = models.CharField(max_length=255,default=None)

    description = models.TextField(max_length=5000 ,default=None)

    pic = models.ImageField(upload_to='images/',height_field=None, width_field=None ,blank=True,null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    date_posted =  models.DateTimeField(default=timezone.now)

    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    # like_count = models.BigIntegerField(default='0')

    objects = UserManager()
    
    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("author", kwargs={'pk':self.pk})

