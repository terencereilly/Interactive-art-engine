

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
	return render(request, "home.html")


def about_view(request):
	return render(request, 'about.html')

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created successfully. You can now log in.')
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})
