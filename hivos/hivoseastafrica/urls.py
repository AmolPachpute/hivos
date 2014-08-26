from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redirect_to/(?P<slug>[a-zA-Z0-9-]+)/$', 'hivoseastafrica.views.redirect_to'),
)

urlpatterns += patterns('',
    url(r'^', include('usermanagement.urls')),
    url(r'^manage/', include('services.urls')),
    url(r'^fund/', include('fundmanagement.urls')),
    url(r'^masterdata/',include('masterdata.urls')),
    url(r'^hr/', include('hrmanagement.urls')),
    url(r'^projects/',include('projects.urls')),
    url(r'^budgets/',include('budget.urls')),
    url(r'^meeting/',include('meeting.urls')),
    url(r'^events/',include('events.urls')),
    url(r'^saccos/',include('saccos.urls')),
    url(r'^app/',include('android_apps.urls')),
    url(r'^farmer/', include('farmer.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^sharemanagement/',include('sharemanagement.urls')),
    url(r'^vam/',include('VAM.urls')),
    url(r'^procurement/',include('procurement.urls')),
    url(r'^reports/',include('reports.urls')),
    url(r'',include('loan_management.urls')),
    url(r'',include('account_management.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
