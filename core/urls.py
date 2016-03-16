from django.conf.urls import patterns, include, url
from django.contrib   import admin
import case
 
urlpatterns = patterns('',
    (r'^color_liker/', include('color_liker.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^case/', include('case.urls', namespace="case")),
    url(r'^sheet/', include('spreadsheet.urls', namespace="sheet")),
    url(r'^dashboard/', include('dashboard.urls', namespace="dashboard")),
        )
