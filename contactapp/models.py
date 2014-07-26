from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime

#Our main model for Contacts 
#Rest of our models have one to one reltionship with this model
class Contact(models.Model):
	user = models.ForeignKey(User, related_name='contacts')
	first_name  = models.CharField(max_length=64)
	last_name = models.CharField(blank=True,null=True, max_length=64)
	email_id = models.CharField(max_length=64)
	mobile_number = models.CharField(blank=True,null=True, max_length=10)
	slug  = models.SlugField(max_length=255,blank=True)
	n_visited = models.IntegerField(blank=True, null=True)
	last_visited = models.DateTimeField(blank=True, default=datetime.now)

	class Meta:
		unique_together = ('user', 'email_id')

	def __unicode__(self):
		return self.first_name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.first_name)
		super(Contact, self).save(*args, **kwargs)

	def get_homecreate_url(self):
		return reverse('contactapp:contacts:homecontactcreate', kwargs={'cpk':self.id})
	def get_socialcreate_url(self):
		return reverse('contactapp:contacts:socialcontactcreate', kwargs={'cpk':self.id})

	def get_officecreate_url(self):
		return reverse('contactapp:contacts:officecontactcreate', kwargs={'cpk':self.id})
	def get_othercreate_url(self):
		return reverse('contactapp:contacts:othercontactcreate', kwargs={'cpk':self.id})

	def get_absolute_url(self):
		return reverse('contactapp:contacts:detail', kwargs={'pk':self.id})

	def get_remove_url(self):
		return reverse('contactapp:contacts:remove', kwargs={'pk':self.id})

	def get_update_url(self):
		return reverse('contactapp:contacts:update', kwargs={'pk':self.id})


class OfficeContact(models.Model):
	contact= models.ForeignKey(Contact, related_name='office')
	company = models.CharField(max_length=100)
	email_id = models.CharField(blank=True, max_length=50, null=True)
	designation = models.CharField(blank=True, max_length=50,null=True)
	telephone_number = models.CharField(blank=True, max_length=50, null=True)
	address = models.CharField(blank=True, max_length=256,null=True)

	def __unicode__(self):
		return self.company

	def get_absolute_url(self):
		return reverse('contactapp:contacts:detail', kwargs={'pk':self.contact_id})
	def get_update_url(self):
		return reverse('contactapp:contacts:officecontactupdate', kwargs={'pk':self.id,'cpk':self.contact_id})

class SocialContact(models.Model):
	SocialSite_Choice=(
		('F','Facebook'),
		('G','Google+'),
		('T','Twitter'),
		)

	contact = models.ForeignKey(Contact, related_name='social')
	social_site = models.CharField(max_length=2, choices= SocialSite_Choice)
	detail = models.CharField(max_length=1024)
	def get_absolute_url(self):
		return reverse('contactapp:contacts:detail', kwargs={'pk':self.contact_id})
	def get_update_url(self):
		return reverse('contactapp:contacts:socialcontactupdate', kwargs={'pk':self.id,'cpk':self.contact_id})

class OtherContact(models.Model):
	contact = models.ForeignKey(Contact, related_name='other')
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('contactapp:contacts:detail', kwargs={'pk':self.contact_id})
	def get_update_url(self):
		return reverse('contactapp:contacts:othercontactupdate', kwargs={'pk':self.id,'cpk':self.contact_id})


class HomeContact(models.Model):
	contact= models.ForeignKey(Contact, related_name='home')
	telephone_number = models.CharField(blank=True, max_length=50,null=True)
	city = models.CharField(max_length=100)
	address = models.CharField(blank=True, max_length=256,null=True)

	def __unicode__(self):
		return self.telephone_number
	def get_absolute_url(self):
		return reverse('contactapp:contacts:detail', kwargs={'pk':self.contact_id})
	def get_update_url(self):
		return reverse('contactapp:contacts:homecontactupdate', kwargs={'pk':self.id,'cpk':self.contact_id})
