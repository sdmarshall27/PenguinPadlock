from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import PasswordTable


def home(request):
	return render(request, 'password/home.html')

class PasswordListView(ListView):
	model=PasswordTable
	template_name='password/list.html'
	context_object_name = 'PasswordTable'

class PasswordCreateView(LoginRequiredMixin, CreateView):
	model = PasswordTable
	fields = ['description', 'password']

	def form_valid(self, form):
		form.instance.owner_id = self.request.user.pk
		return super().form_valid(form)

class PasswordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = PasswordTable
	fields = ['description', 'password']

	def form_valid(self, form):
		form.instance.owner_id = self.request.user.pk
		return super().form_valid(form)

	def test_func(self):
		password = self.get_object()
		if self.request.user.id == password.owner_id:
			return True
		return False

class PasswordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = PasswordTable
	success_url = '/password/list'

	def test_func(self):
		password = self.get_object()
		if self.request.user.id == password.owner_id:
			return True
		return False

@login_required
def list(request):
	all_passwords = PasswordTable.objects.filter(owner_id=request.user.pk)
	context = {
		'title': "Passwords",
		'PasswordTable': all_passwords,
	}
	return render(request, 'password/list.html', context)