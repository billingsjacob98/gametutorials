from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tutorials.views.home', name='home'),

    url(r'^games/', include('tutorials.urls')),

    url(r'^get_games/', 'tutorials.views.get_games', name='get_games'),

    url(r'^admin/', include(admin.site.urls)),
)
