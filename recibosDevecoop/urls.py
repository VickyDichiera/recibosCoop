from django.conf.urls import patterns, include, url
from django.contrib import admin
from recibos.views import WithdrawalView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recibosDevecoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<withdrawal_id>\d+)$', WithdrawalView.as_view(), name='Withdrawal'),
)
