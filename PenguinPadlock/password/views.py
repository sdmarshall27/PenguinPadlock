from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Alexander',
		'title': 'Post 1',
		'content': 'My content'
	},
	{
		'author': 'Dwight',
		'title': 'Post 1',
		'content': 'Beets'
	}
]

def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'password/home.html', context)

def list(request):
	return render(request, 'password/list.html', {'title': 'List'})