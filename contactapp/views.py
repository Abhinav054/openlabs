from __future__ import absolute_import
from django.shortcuts import render
from . import models
from braces import views
from django.views import generic
from datetime import datetime
from . import forms
from django.http import Http404
from django.contrib import messages
from django.core.urlresolvers import reverse


# restricts querys to be restricted to the current user loggedin
class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset



# Create your views here.

class ContactListView(views.LoginRequiredMixin, generic.ListView):
	model = models.Contact

	def get_queryset(self):
		return self.request.user.contacts.all()


class ContactDetailView(views.LoginRequiredMixin, generic.DetailView):
	# """docstring for ContactDetailView"""
	# def __init__(self, arg):
	# 	super(ContactDetailView, self).__init__()
	# 	self.arg = arg
	model = models.Contact
	# prefetch_related = ('home','social')

	def get_object(self):
		obj = super(ContactDetailView, self).get_object()
		obj.last_visited = datetime.now()
		obj.n_visited =+1
		obj.save()
		return obj
		
class ContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	# """docstring for ContactCreateView"""
	# def __init__(self, arg):
	# 	super(ContactCreateView, self).__init__()
	# 	self.arg = arg
	form_class = forms.ContactForm
	headline = 'Create'
	model = models.Contact

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(ContactCreateView, self).form_valid(form)




class ContactUpdateView(RestrictToUserMixin, views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.ContactForm
	headline = 'Update'
	model = models.Contact

class HomeContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.HomeForm
	headline = 'Add'
	model = models.HomeContact
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(HomeContactCreateView, self).form_valid(form)




class OfficeContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.OfficeForm
	headline = 'Add'
	model = models.OfficeContact
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(OfficeContactCreateView, self).form_valid(form)



class SocialContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.SocialForm
	headline = 'Add'
	model = models.SocialContact
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(SocialContactCreateView, self).form_valid(form)

class OtherContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.OtherForm
	headline = 'Add'
	model = models.OtherContact
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(OtherContactCreateView, self).form_valid(form)


class HomeContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.HomeForm
	headline = 'Update'
	model = models.HomeContact


class OfficeContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.OfficeForm
	headline = 'Update'
	model = models.OfficeContact

class SocialContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.SocialForm
	headline = 'Update'
	model = models.SocialContact

class OtherContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.OtherForm
	headline = 'Update'
	model = models.OtherContact

class ContactRemoveView(views.LoginRequiredMixin, generic.RedirectView):

	model = models.Contact
	def get_redirect_url(self,*args,**kwargs):
		return reverse('contactapp:contacts:list')
	def get_object(self,pk):
		try:
			contact = self.model.objects.get(
				pk=pk,
				user=self.request.user)
		except models.Contact.DoesNotExist:
			raise Http404
		else:
			return contact

	def get(self, request, *args, **kwargs):
		self.object = self.get_object(kwargs.get('pk'))
		messages.success(
			request,
			u'{0.first_name} {0.last_name} was removed'.format(
                self.object))
		self.object.delete()
		return super(ContactRemoveView, self).get(request, *args, **kwargs)
