from django.shortcuts import render
from django.http import HttpResponse
from .models import PasswordTable


def home(request):
	context = {
		'PasswordTable': PasswordTable.objects.all()
	}
	return render(request, 'password/home.html', context)

def list(request):
	return render(request, 'password/list.html', {'title': 'List'})