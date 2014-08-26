from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'hrmanagement.views.home', name='home'),
    url(r'^main-data/', 'hrmanagement.views.main_data', name='hr-main-data'),
    url(r'^staffs/(?P<task>(:?list|:?add|:?edit|:?delete|:?active))/$',
                                    'hrmanagement.views.manage_staff',
                                    name='hr-manage-staff'),

    url(r'^staff-address/(?P<task>(:?list|:?add|:?edit|:?delete|:?active))/$',
                                    'hrmanagement.views.manage_staff_address',
                                    name='hr-manage-staff-address'),

    url(r'^salary/(?P<task>(:?list|:?add|:?edit|:?delete|:?active))/$',
                                    'hrmanagement.views.manage_salary',
                                    name='hr-manage-salary'),
    url(r'^payment/(?P<task>(:?list|:?add|:?edit|:?delete|:?active))/$',
                                    'hrmanagement.views.manage_payment',
                                    name='hr-manage_payment'),

    url(r'^payment-details/$', 'hrmanagement.views.payment_details', name='hr-payment_details'),

    url(r'^get_county/$', 'hrmanagement.views.get_county', name='hr-get-county'),  # for ajax request to get county for that state

)
