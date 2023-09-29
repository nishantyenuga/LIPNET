# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('upload', views.video_upload,name='upload'),
    path('forum', views.disussion,name='forum'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
# # urls.py

# from django.urls import path
# from apps.home.views import location_view


# urlpatterns = [
#     path('location/', location_view, name='location'),
# ]
