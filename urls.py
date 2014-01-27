from django.conf.urls import patterns, include, url
from django.views.generic.list_detail import object_list
from quirktonomicon.views import IdeationListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quirktonomicon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'ideas?/(\d*)$', 'quirktonomicon.views.votes_plot'),
    url(r'ideas?/', IdeationListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
