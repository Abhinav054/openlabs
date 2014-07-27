from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from . import views

lists_patterns = patterns(
	'',
	url(r'^/create/$',views.ContactBookCreateView.as_view(),name='cbcreate'),
	url(r'^(?P<cbpk>[-\w]+)/$',views.ContactListView.as_view(),name='list'),
	url(r'^cb/(?P<cbpk>[-\w]+)/create/',views.ContactCreateView.as_view(),name='contactcreate'),
	url(r'^(?P<cbpk>[-\w]+)/update/(?P<pk>[-\w]+)/$', views.ContactUpdateView.as_view(),
    name='update'),
	url(r'^(?P<cbpk>[-\w]+)/d/(?P<pk>[-\w]+)/$',views.ContactDetailView.as_view(),name='detail'),
	url(r'^(?P<cbpk>[-\w]+)/remove/(?P<pk>[-\w]+)/$',views.ContactRemoveView.as_view(),name='remove'),
	url(r'^(?P<cbpk>[-\w]+)/home/(?P<cpk>[-\w]+)/create/$', views.HomeContactCreateView.as_view(),name='homecontactcreate'),
	url(r'^(?P<cbpk>[-\w]+)/office/(?P<cpk>[-\w]+)/create/$', views.OfficeContactCreateView.as_view(),name='officecontactcreate'),
	url(r'^(?P<cbpk>[-\w]+)/other/(?P<cpk>[-\w]+)/create/$', views.OtherContactCreateView.as_view(),name='othercontactcreate'),
	url(r'^(?P<cbpk>[-\w]+)/social/(?P<cpk>[-\w]+)/create/$', views.SocialContactCreateView.as_view(),name='socialcontactcreate'),
	url(r'^(?P<cbpk>[-\w]+)/social/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.SocialContactUpdateView.as_view(),name='socialcontactupdate'),
	url(r'^(?P<cbpk>[-\w]+)/home/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.HomeContactUpdateView.as_view(),name='homecontactupdate'),
	url(r'^(?P<cbpk>[-\w]+)/office/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.OfficeContactUpdateView.as_view(),name='officecontactupdate'),
	url(r'^(?P<cbpk>[-\w]+)/other/(?P<cpk>[-\w]+)/update/(?P<pk>[-\w]+)$', views.OtherContactUpdateView.as_view(),name='othercontactupdate'),
	url(r'^cb/search/$',views.SearchView.as_view(),name='search'),
	)
	
urlpatterns = patterns(
	'',
	url(r'^contacts/',include(lists_patterns, namespace = 'contacts'))
	)
