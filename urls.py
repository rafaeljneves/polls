from django.conf.urls import patterns, include, url

from polls import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^polls/$', views.index , name='index'),
    # ex.: /polls/5
    url(r'^polls/(?P<poll_id>\d+)/$', views.details, name='details'),
    # ex.: /polls/5/results
    url(r'^polls/(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex.: /polls/5/vote
    url(r'^polls/(?P<poll_id>\d+)/vote/$', views.vote,  name='vote'),
    # ex.: /time
    url(r'^time/$', views.hora_certa, name='hora_certa'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
