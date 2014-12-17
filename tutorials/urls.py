from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^list/', 'tutorials.views.games', name='games'),
    url(r'^(?P<game_id>[0-9]+)/$', 'tutorials.views.detail', name='detail'),
)
