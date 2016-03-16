__author__ = 'chris'
from django.conf.urls import patterns, include, url
import views

# noinspection PyInterpreter
urlpatterns = patterns('',

    url(r'^main/$', 'dashboard.views.main'),
    url(r'^benefitsgraph/$', 'dashboard.views.benefitsgraph'),
    url(r'^summarygraph/$', 'dashboard.views.summarygraph'),
    url(r'^capital_costs/$', 'dashboard.views.capital_costs'),
    url(r'^revenue/$', 'dashboard.views.revenue'),
                       )
