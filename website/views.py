from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('<h1> Home </h1>')

def about(request):
	return HttpResponse('<h1> About </h1>')

def login(request):
	return HttpResponse('<h1>login </h1>')

def registration(request):
	return HttpResponse('<h1> registration')


