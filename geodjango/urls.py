from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

from django.contrib import admin
## Only during Devellopment  ##
from django.conf import settings
#######

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
        # static files (images, css, javascript, etc.)
        urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))
