from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import Project

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()  
    return render(request, 'index.html', {"projects": projects})

def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awardss/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awardss/search.html',{"message":message})