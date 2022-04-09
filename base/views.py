from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from base.models import Project

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()  
    return render(request, 'index.html', {"projects": projects})