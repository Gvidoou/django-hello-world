from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django_hello_world.hello import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.PersonView.as_view(), name='home'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
