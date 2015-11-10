__author__ = 'chris'
from django.conf.urls  import patterns, include, url

urlpatterns = patterns('',
   url(r"^dimension_(?P<dimension_number>\d+)/$", "case.views.dimension"),
   url(r"^scoring_(?P<score_number>\d+)/$", "case.views.scoring"),
   url(r'^', 'case.views.index'),
)
