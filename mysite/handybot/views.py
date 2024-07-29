from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

def index(request):
    project_list = Project.objects.order_by("project_name")[:3]
    context = {"project_list": project_list}
    return render(request, "handybot/index.html", context)

def project_detail(request, project_id):
    return HttpResponse("You are looking at project %s." % project_id)

def suggestions(request, project_id):
    response = "You are looking at the suggested tools for project %s."
    return HttpResponse(response % project_id)

def save_tools(request, project_id):
    return HttpResponse("You are saving tools for project %s." % project_id) 

def list_saved(reuest, project_id):
    return HttpResponse("You are looking at saved tools for project %s." % project_id)