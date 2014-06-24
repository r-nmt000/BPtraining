from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from necommend.models import Neco


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BPtraining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 
      ListView.as_view(
        queryset=Neco.objects.all(),
        context_object_name='neco_list',
        template_name='index.html')),
    url(r'^(?P<pk>\d+)/$',
      DetailView.as_view(
        model=Neco,
        template_name='detail.html')),
)
