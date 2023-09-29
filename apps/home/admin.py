# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import uploadedVid
admin.site.register(uploadedVid)

from .models import forum
admin.site.register(forum)