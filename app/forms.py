from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post, Comment

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Password'}),
        }

    #username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control','style': 'width: 30rem;'}),
            'image': forms.FileInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
        }