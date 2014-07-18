from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BPtraining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^necommend/', include('necommend.urls')),
)


#api
urlpatterns += patterns('BPtraining.apis',
    url(r'^api/neco/$', 'neco_list'),
    url(r'^api/neco/(?P<neco_id>\d)/$', 'neco_detail'),
    )

