from __future__ import absolute_import
from django.views import generic
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from braces import views
from django.db.models import Count
from django.shortcuts import redirect
from contactapp.models import ContactBook


class HomePageView(generic.ListView):
    template_name = 'home.html'
    model = ContactBook
    def get_queryset(self):
    	if self.request.user.is_authenticated():
    		queryset = super(HomePageView, self).get_queryset()
    		queryset = queryset.filter(user=self.request.user)
    		queryset = queryset.annotate(contact_count=Count('contacts')) 
    		return queryset
	    		
			

class SignUpView(generic.CreateView, views.AnonymousRequiredMixin, views.FormValidMessageMixin):
	form_class = RegistrationForm
	form_valid_message = 'Your Account has been Successfully Created'
	model = User
	success_url = reverse_lazy('home')
	template_name = 'accounts/signup.html'
	def form_valid(self, form):
		resp = super(SignUpView, self).form_valid(form)
		ContactBook.objects.create(user=self.object, name='My Book')
		return resp

class LoginView(generic.FormView, views.AnonymousRequiredMixin, views.FormValidMessageMixin):
	form_class = LoginForm
	form_valid_message = 'You are now Logged-in'
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'
	def form_valid(self,form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username = username, password = password)
		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)


# class LogOutView(generic.RedirectView, views.LoginRequiredMixin):
# 	url = reverse_lazy('home')

# 	def get(self, request, *args, **kwargs):
# 		logout(request)
# 		return super(LogOutView, self).get(request, *args, **kwargs)
def LogOutView(request):
	logout(request)
	return redirect(reverse('home'))
