# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from django import template
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.urls import reverse
# from .LipNet import *
# from .models import uploadedVid
# from .forms import vidForm,forumForm
# from django.conf import settings


# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}

#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))

# def disussion(request):
#     d=forumForm(request.POST or None)
#     if d.is_valid():
#         obj = d.save(commit=False)
#         obj.save()
#         name=obj.user_name
#         ans=obj.answer

#     context={'name':name,'ans':ans}

#     html_template = loader.get_template('home/forum.html')
#     return HttpResponse(html_template.render(context, request))


# def video_upload(request):
#     a = vidForm(request.POST or None, request.FILES or None)
#     if a.is_valid():
#         obj = a.save(commit=False)
#         obj.save()
#         s=obj.video.url.split('/')[-1]
#         s1=s.split("_")
#         print(s1[0])
#         v_path=obj.video.url
#         v_path=s1[0]
#         print(v_path)
#         n=v_path.split(".")
#         name=n[0]
#         print(name)

#         output=lipOut(v_path)
#         # output=lipOut(v)
#         # output='hi'
#     context={'output':output,'v_path':v_path,'name': name}

#     html_template = loader.get_template('home/upload.html')
#     return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .LipNet import *
from .models import uploadedVid
from .forms import vidForm,forumForm
from django.conf import settings


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def disussion(request):
    d=forumForm(request.POST or None)
    if d.is_valid():
        obj = d.save(commit=False)
        obj.save()
        name=obj.user_name
        ans=obj.answer

    context={'name':name,'ans':ans}

    html_template = loader.get_template('home/forum.html')
    return HttpResponse(html_template.render(context, request))


# def video_upload(request):
#     a = vidForm(request.POST or None, request.FILES or None)
#     if a.is_valid():
#         obj = a.save(commit=False)
#         obj.save()
#         s=obj.video.url.split('/')[-1]
#         s1=s.split("_")
#         print(s1[0])
#         v_path=obj.video.url
#         v_path=s1[0]
#         print(v_path)
#         n=v_path.split(".")
#         name=n[0]
#         con='-converted'
#         if con in name:
#             name=name+"-converted"
#             print(name)
#         else:
#             print(name)

#         output=lipOut(v_path)
#         # output=lipOut(v)
#         # output='hi'
#     context={'output':output,'v_path':v_path,'name': name}

#     html_template = loader.get_template('home/upload.html')
#     return HttpResponse(html_template.render(context, request))
def video_upload(request):
    a = vidForm(request.POST or None, request.FILES or None)
    if a.is_valid():
        obj = a.save(commit=False)
        obj.save()
        s=obj.video.url.split('/')[-1]
        s1=s.split("_")
        print(s1[0])
        v_path=obj.video.url
        v_path=s1[0]
        print(v_path)
        n=v_path.split(".")
        name=n[0]
        name=name+"-converted"
        print(name)

        output=lipOut(v_path)
        # output=lipOut(v)
        # output='hi'
    context={'output':output,'v_path':v_path,'name': name}

    html_template = loader.get_template('home/upload.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

from django.shortcuts import render
from django.conf import settings

def location_view(request):
    return render(request, 'location.html', {'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY})
