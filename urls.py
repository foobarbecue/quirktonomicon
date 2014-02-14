from django.conf.urls import patterns, include, url
from quirktonomicon.views import IdeationListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quirktonomicon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IdeationListView.as_view()),    
    url(r'ideas?/?$', IdeationListView.as_view()),
    url(r'ideas?/(\d*)$', 'quirktonomicon.views.votes_plot'),
    url(r'ideas?_json/(\d*)$', 'quirktonomicon.views.idea_json'),
    url(r'cloud/?$', 'quirktonomicon.views.cloud'),
    url(r'votes_plot_json/(\d*)$', 'quirktonomicon.views.votes_plot_json'),
    url(r'flag?/?$', 'quirktonomicon.views.flag'),
    url(r'stats?/?$', 'quirktonomicon.views.stats_view'),
    url(r'^admin/', include(admin.site.urls)),
)
