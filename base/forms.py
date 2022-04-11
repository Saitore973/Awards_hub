from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import  Profile, Project
from django.forms import EmailInput, TextInput, PasswordInput, FileInput 


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
        
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image','title','description','link']
        
        
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePhoto','bio']

# class SearchForm(forms.Form):
#     name = forms.CharField(max_length=30)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilePhoto', 'bio' ]
        # widgets = {
        #     'avatar': FileInput(attrs={'class': 'form-control my-1'}),
        #     'firstName': TextInput(attrs={'class': 'form-control my-1'}),
        #     'lastName': TextInput(attrs={'class': 'form-control my-1'}),
        #     'bio': TextInput(attrs={'class': 'form-control my-1'}),
            
        # }