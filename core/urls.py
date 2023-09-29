# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

from apps.home.views import location_view  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    path('location/', location_view, name='location'),
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
# urls.py

# from django.urls import path
# from apps.home.views import location_view


# urlpatterns = [
#     path('location/', location_view, name='location'),
# ]
