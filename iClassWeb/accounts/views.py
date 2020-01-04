from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import StudentSignupForm, TeacherSignupForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request):	
	return render(request, 'base.html')


class SignupView(TemplateView):
	template_name = 'accounts/signup.html'


class TeacherSignupView(CreateView):
	User = get_user_model()
	model = User
	form_class = TeacherSignupForm
	template_name = 'accounts/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('index')


class StudentSignupView(CreateView):
	User = get_user_model()
	model = User
	form_class = StudentSignupForm
	template_name = 'accounts/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('index')


@method_decorator([login_required], name='dispatch')
class View_Profile(TemplateView):
	template_name = 'accounts/profile.html'


@method_decorator([login_required], name='dispatch')
class Edit_Profile(UpdateView):
	User = get_user_model()
	model = User
	fields = ['first_name', 'last_name', 'image']
	template_name = 'accounts/edit_profile.html'
	success_url = reverse_lazy('view_profile')


@method_decorator([login_required], name='dispatch')
class Delete_Account(DeleteView):
	User = get_user_model()
	model = User
	template_name = 'accounts/delete_account.html'
	success_url = reverse_lazy('index')




	