from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  ProjectForm, ProfileForm
from base.models import Project, Profile
from .forms import UserRegistrationForm,EditProfileForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()  
    return render(request, 'index.html', {"projects": projects})


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awardss/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awardss/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ValueError:
        raise Http404()
    return render(request,"awardss/project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def profile(request, id):
    profile = Profile.objects.get(user=id)
    userid = request.user.id
    form = ProfileForm(instance=profile)

    return render(request, 'awardss/profile.html',{"profile":profile,"form":form, "userid":userid})


@login_required(login_url='/accounts/login/')
def create(request):
    form = ProjectForm()
    userid = request.user.id
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            title = form.cleaned_data['title']
            link = form.cleaned_data['link']
            description = form.cleaned_data['description']
            user_of_post = request.user
            post = Project(image=image,title=title, description=description,user=user_of_post)
            post.save()
            return redirect('welcome')
    return render(request, 'awardss/create.html', {"form":form,"userid":userid})


@login_required(login_url='/accounts/login/')
def edit(request, id):
    form = ProfileForm()
    userid = request.user.id
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profilePhoto = form.cleaned_data['profilePhoto']
            bio = form.cleaned_data['bio']
            user_of_post = request.user
            post = Profile(profilePhoto=profilePhoto,bio=bio, user=user_of_post)
            post.save()
            return redirect('welcome')
    return render(request, 'awardss/edit.html', {"form":form})


def rate(request):
    form = ProjectForm()
    userid = request.user.id
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            user_of_post = request.user
            post = Project(image=image,title=title, description=description,user=user_of_post)
            post.save()
            return redirect('welcome')
    return render(request, 'awardss/rate.html', {"form":form,"userid":userid})