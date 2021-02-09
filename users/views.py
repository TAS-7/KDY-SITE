from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
	
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} your account has been created!')
			return redirect('login')
	else:
		#redirect the user if they are already signed in 
		if request.user.is_authenticated:
			return redirect('website-home')

		else:
			form = UserRegisterForm()
			return render(request, 'users/register.html', {'form': form})

def profile(request):
	if request.user.is_authenticated:
		return render(request, 'users/profile.html')
	else:
		return redirect('login')

# message option tags
#message.success
#message.debug
#message.info
#message.warning
#message.error