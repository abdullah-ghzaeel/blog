from collections import defaultdict
from typing import DefaultDict
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,null=True,blank=True)
    content=RichTextField()
    img=models.ImageField(upload_to='post_img/', default ='post_img/default.png')
    created=models.DateTimeField(default=timezone.now)
    active = BooleanField(default=True)
    def __str__(self):
        return self.title
