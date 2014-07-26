from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from . import views

lists_patterns = patterns(
	'',
	url(r'^$',views.ContactListView.as_view(),name='list'),
	url(r'^create/$',views.ContactCreateView.as_view(),name='create'),
	url(r'^update/(?P<pk>[-\w]+)/$', views.ContactUpdateView.as_view(),
    name='update'),
	url(r'^d/(?P<pk>[-\w]+)/$',views.ContactDetailView.as_view(),name='detail'),
	url(r'^remove/(?P<pk>[-\w]+)/$',views.ContactRemoveView.as_view(),name='remove'),
	url(r'^home/(?P<cpk>[-\w]+)/create/$', views.HomeContactCreateView.as_view(),name='homecontactcreate'),
	url(r'^office/(?P<cpk>[-\w]+)/create/$', views.OfficeContactCreateView.as_view(),name='officecontactcreate'),
	url(r'^other/(?P<cpk>[-\w]+)/create/$', views.OtherContactCreateView.as_view(),name='othercontactcreate'),
	url(r'^social/(?P<cpk>[-\w]+)/create/$', views.SocialContactCreateView.as_view(),name='socialcontactcreate'),
	url(r'^social/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.SocialContactUpdateView.as_view(),name='socialcontactupdate'),
	url(r'^home/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.HomeContactUpdateView.as_view(),name='homecontactupdate'),
	url(r'^office/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.OfficeContactUpdateView.as_view(),name='officecontactupdate'),
	url(r'^other/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.OtherContactUpdateView.as_view(),name='othercontactupdate'),
	)
	
urlpatterns = patterns(
	'',
	url(r'^contacts/',include(lists_patterns, namespace = 'contacts'))
	)
