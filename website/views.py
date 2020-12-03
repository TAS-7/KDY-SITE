from django.shortcuts import render


# view for home page
def home(request):
	return render(request, 'website/home.html')


# view for about page
def about(request):
	return render(request, 'website/about.html')




