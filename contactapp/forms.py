from __future__ import absolute_import
from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class ContactForm(forms.ModelForm):
    class Meta:
    	model = models.Contact
    	fields = ['first_name', 'last_name', 'email_id', 'mobile_number']

    def __init__(self, *args, **kwargs):
    	super(ContactForm, self).__init__(*args, **kwargs)
    	self.helper = FormHelper()
    	self.helper.layout = Layout(
    		'first_name',
    		'last_name',
    		'email_id',
    		'mobile_number',
    		ButtonHolder(
    			Submit('create','Create')
    		)
    	)

class HomeForm(forms.ModelForm):
    class Meta:
        model = models.HomeContact
        fields = ['telephone_number','city','address']
    

    def __init__(self,*args,**kwargs):
        super(HomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'telephone_number',
            'city',
            'address',
            ButtonHolder(
                Submit('create','Create')
            )
        )
class SocialForm(forms.ModelForm):
    class Meta:
        model = models.SocialContact
        fields = ['social_site','detail']
    

    def __init__(self,*args,**kwargs):
        super(SocialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'social_site',
            'detail',
            ButtonHolder(
                Submit('create','Create')
            )
        )

class OfficeForm(forms.ModelForm):
    class Meta:
        model = models.OfficeContact
        fields = ['company','email_id','telephone_number','designation','address']
    

    def __init__(self,*args,**kwargs):
        super(OfficeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'company',
            'email_id',
            'telephone_number',
            'designation',
            'address',
            ButtonHolder(
                Submit('create','Create')
            )
        )


class OtherForm(forms.ModelForm):
    class Meta:
        model = models.OtherContact
        fields = ['name','details',]
    

    def __init__(self,*args,**kwargs):
        super(OtherForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'details',
            ButtonHolder(
                Submit('create','Create')
            )
        )
