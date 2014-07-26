from __future__ import absolute_import
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Contact)
admin.site.register(models.SocialContact)
admin.site.register(models.HomeContact)
admin.site.register(models.OfficeContact)
admin.site.register(models.OtherContact)
