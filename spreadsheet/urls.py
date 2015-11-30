__author__ = 'chris'
from django.conf.urls import patterns, url
from django.conf import settings
from .views import index

urlpatterns = patterns('',
    ( r'^resources/(?P<path>.*)$',
      'django.views.static.serve',
      { 'document_root': settings.MEDIA_ROOT } ),
    url( r'^spreadsheet_app/', index, name="index"),
)