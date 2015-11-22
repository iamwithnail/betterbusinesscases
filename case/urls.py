__author__ = 'chris'
from django.conf.urls  import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'^options/new/(?P<dimension>[^/]+)/$', views.options_new, name='options_new'),
    url(r'^options/new/$', views.options_new, name='options_new'),
    url(r'^options/(?P<pk>[0-9]+)/$', views.options_detail, name='options_detail'),
    url(r'^options/(?P<pk>[0-9]+)/edit/$', views.options_edit, name='options_edit'),
    url(r'^options/(?P<dimension>[^/]+)/$', 'case.views.options_main'),
    url(r'^options/$', 'case.views.options_main'),
    #url(r'^dimension_(?P<dimension_number>\d+)/$', 'case.views.dimension'),
    url(r'^scoring_(?P<score_number>\d+)/$', 'case.views.scoring'),
    url(r'^graph/$', 'case.views.graphtest'),


    #url(r'^score/(?P<option>[^/]+)/$', ('case.views.scoring')),
    url(r'^', 'case.views.index'),
)
