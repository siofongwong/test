from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import dbhelper

# Create your views here.
def login(request):
    return render_to_response("sc1/login.html")

@csrf_exempt
def home(request):
    return render_to_response("sc1/home.html", {"projects": dbhelper.query_project()})

@csrf_exempt
def create_project(request):
    return render_to_response("sc1/create_project.html")

@csrf_exempt
def project(request, title):
    return render_to_response("sc1/project.html", {"title": title})

@csrf_exempt
def save_project(request, title, git_link):
    dbhelper.create_project(title, git_link)
    return render_to_response("sc1/project.html", {"title": title})

