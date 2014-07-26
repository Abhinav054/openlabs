from django.conf.urls import patterns, include, url
from .views import HomePageView
from .views import SignUpView
from .views import LoginView
from .views import LogOutView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openlabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomePageView.as_view(),name='home'),
    url(r'^accounts/register/$',SignUpView.as_view(),name='signup'),
    url(r'^accounts/login/$',LoginView.as_view(),name='login'),
    url(r'^accounts/logout/$',LogOutView,name='logout'),
    url(r'^contactapp/',include('contactapp.urls',namespace = 'contactapp'))

)
