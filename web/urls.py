from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'image.views.home', name='home'),
    url(r'^image/', 'image.views.home', name='home'),
	url(r'^get_query/', 'image.views.get_query'),
)
