# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.validators import FileExtensionValidator


# Create your models here.
class uploadedVid(models.Model):
    video_name = models.CharField(max_length=10,default=True)
    video = models.FileField(upload_to='videos_uploaded/',null=True,default=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv','mpg'])])

    def __str__(self):
        return self.video_name
    
class forum(models.Model):
    user_name=models.CharField(max_length=20,default=True)
    answer=models.TextField(max_length=500,default=True)

    def __str__(self):
        return self.user_name

