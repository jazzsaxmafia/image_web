from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'image.views.home'),
    url(r'^image/', 'image.views.image'),
	url(r'^news/', 'news.views.news'),
	url(r'^get_image/', 'image.views.get_query'),
	url(r'^get_news/', 'news.views.get_query'),
	url(r'^socialpick/', 'image.views.socialpick'),
)
