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
from . import utils



# restricts querys to be restricted to the current user loggedin
class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset



# Create your views here.

class ContactListView(views.LoginRequiredMixin, generic.ListView):
	model = models.Contact

	def get_context_data(self, **kwargs):
		create_url = self.kwargs['cbpk']
		create_url = reverse('contactapp:contacts:contactcreate',kwargs={'cbpk':create_url})
		context = super(ContactListView, self).get_context_data(**kwargs)
		context['create_url'] = create_url
		return context

	def get_queryset(self):
		queryset = super(ContactListView, self).get_queryset()
		queryset = queryset.filter(contact_book = self.kwargs['cbpk'])
		return queryset


class ContactDetailView(views.LoginRequiredMixin, generic.DetailView):
	# """docstring for ContactDetailView"""
	# def __init__(self, arg):
	# 	super(ContactDetailView, self).__init__()
	# 	self.arg = arg
	model = models.Contact
	# prefetch_related = ('home','social')

	def get_context_data(self, **kwargs):
		cbpk = self.kwargs['cbpk']
		back_url = reverse('contactapp:contacts:list',kwargs={'cbpk':cbpk})
		context = super(ContactDetailView, self).get_context_data(**kwargs)
		context['cbpk'] = cbpk
		context['back_url'] = back_url
		return context



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
		self.object.contact_book_id = self.kwargs['cbpk']
		self.object.save()
		return super(ContactCreateView, self).form_valid(form)




class ContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.ContactForm
	headline = 'Update'
	model = models.Contact


class HomeContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.HomeForm
	headline = 'Add'
	model = models.HomeContact
	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(HomeContactCreateView, self).form_valid(form)




class OfficeContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.OfficeForm
	headline = 'Add'
	model = models.OfficeContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(OfficeContactCreateView, self).form_valid(form)



class SocialContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.SocialForm
	headline = 'Add'
	model = models.SocialContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(SocialContactCreateView, self).form_valid(form)

class OtherContactCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
	form_class = forms.OtherForm
	headline = 'Add'
	model = models.OtherContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.contact_id = self.kwargs['cpk']
		self.object.save()
		return super(OtherContactCreateView, self).form_valid(form)


class HomeContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.HomeForm
	headline = 'Update'
	model = models.HomeContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})


class OfficeContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.OfficeForm
	headline = 'Update'
	model = models.OfficeContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

class SocialContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.SocialForm
	headline = 'Update'
	model = models.SocialContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

class OtherContactUpdateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.UpdateView):
	form_class = forms.OtherForm
	headline = 'Update'
	model = models.OtherContact

	def get_success_url(self):
		return reverse('contactapp:contacts:detail',kwargs={'cbpk':self.kwargs['cbpk'],'pk':self.kwargs['cpk']})

class ContactRemoveView(views.LoginRequiredMixin, generic.RedirectView):

	model = models.Contact
	def get_redirect_url(self,*args,**kwargs):
		return reverse('contactapp:contacts:list',kwargs={'cbpk':self.kwargs['cbpk']})
	def get_object(self,pk):
		try:
			contact = self.model.objects.get(
				pk=pk)
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




class SearchView(views.LoginRequiredMixin, generic.TemplateView):
	
	template_name = 'search.html'

	def get_context_data(self, **kwargs):
		query_string = ''
		found_entries = None
		if ('q' in self.request.GET) and self.request.GET['q'].strip():
			query_string = self.request.GET['q']
			contact_query = utils.get_query(query_string,['first_name','last_name'])
			found_entries = models.Contact.objects.filter(contact_query, contact_book__user = self.request.user).order_by('last_visited')
		context = super(SearchView, self).get_context_data(**kwargs)
		context['searchobject'] = found_entries
		return context

class ContactBookCreateView(views.LoginRequiredMixin, generic.RedirectView):
	model = models.ContactBook

	def get_redirect_url(self,*args,**kwargs):
		return reverse('home')


	def get(self, request, *args, **kwargs):
		self.object = models.ContactBook(name=self.request.GET['name'], user=self.request.user)
		self.object.save()
		return super(ContactBookCreateView, self).get(request, *args, **kwargs)
