from django.shortcuts import render
from . models import Post, Comment


# view for home page
def home(request):
	context = {
	     'posts': Post.objects.all(),
	     'comments' : Comment.objects.all()
	}
	return render(request, 'website/home.html')


# view for about page
def about(request):
	return render(request, 'website/about.html')


