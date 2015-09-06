from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
import tinymce
import textarea.views

print 1234
urlpatterns = patterns('',
    url(r'^$', textarea.views.index, name='index'),
    url(r'^upload', 'textarea.views.upload'),
    url(r'^ondrop', 'textarea.views.ondrop'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,  }),
    url(r'^equation_editor.html', textarea.views.index1, name='index1'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)
