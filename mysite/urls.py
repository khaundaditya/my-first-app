import django
from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include('account.urls')),
    url(r'^reports/',include('reports.urls',namespace="reports")),
    url(r'^reviewer/',include('reviewer.urls',namespace="reviewer")),
    url(r'^messages/', include('django_messages.urls')),
]

try:
    import ajax_select
    # If django-ajax-selects is installed, include its URLs:
    urlpatterns += patterns('',
        url(r'^ajax-select/', include('ajax_select.urls'))
    )
except ImportError:
    pass

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.STATIC_URL[1:-1],
         'django.views.static.serve',
         {'document_root':  settings.STATIC_ROOT, 'show_indexes': False}),
    )
