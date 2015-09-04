from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import tinymce
import textarea.views

urlpatterns = patterns('',
    url(r'^$', textarea.views.index, name='index'),
    url(r'^upload/', textarea.views.upload, name='upload'),
    url(r'^equation_editor.html', textarea.views.index1, name='index1'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)
