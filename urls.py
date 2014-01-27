from django.conf.urls import patterns, include, url
from quirktonomicon.views import IdeationListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quirktonomicon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'ideas?/?$', IdeationListView.as_view()),
    url(r'ideas?/(\d*)$', 'quirktonomicon.views.votes_plot'),    
    url(r'^admin/', include(admin.site.urls)),
)
