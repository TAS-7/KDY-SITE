from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#education levels are High School level && Tertiary level
educationlevel = [('Level2', 'High School'),('Level3', 'Tertiary') ]
levels = [('lvl10', 'Grade 10'), ('lvl11', 'Grade 11'), ('lvl12', 'Grade 12'),('lvl13', 'YOS 1'), ('level14', 'YOS 2'), ('level15', 'YOS 3')]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    education= forms.CharField(widget=forms.Select(choices=educationlevel))
    level =forms.CharField(widget=forms.Select(choices=levels))
    subjects = forms.CharField(help_text ='Please enter the subjects you need assistance with.')

    class Meta:
        model = User
        fields = ['username', 'email','education', 'level', 'subjects' ,'password1', 'password2']