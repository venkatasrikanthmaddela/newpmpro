from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template

from newpmpro.models import ProjectData, ProjectRequests


def home_page(request):
    try:
        if request.request.email:
            return render(request, 'home.html', {"request":request})
    except:
        return render(request, 'home.html', {})


def new_project_idea_page(request):
    try:
        if request.request.email:
            return render(request, 'newProjectIdea.html', {"request":request})
    except:
        return render(request, 'newProjectIdea.html', {})


def search_project_page(request):
    project_data = ProjectData.objects.all()
    requested_projects = list()
    try:
        if request.user.email:
            requested_projects = ProjectRequests.objects.filter(user__email=request.user.email).values_list('projectInfo__id', flat=True)
            return render(request, 'searchProjectManagement/searchProjects.html', {"projectData": project_data,
                                                                                   "requestedProjects": requested_projects})
    except:
        return render(request, 'searchProjectManagement/searchProjects.html',
                      {"projectData": project_data, "requestedProjects": requested_projects})