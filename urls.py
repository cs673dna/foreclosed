from django.conf.urls.defaults import *
from views import index
from hamp.hamp import HAMP
from foreclosure_probability.foreclosure_probability import foreclosure_probability
from models import HAMP_new

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),
	#(r'hamp', HAMPResults),
	#(r'administrate', administrate),
	(r'hamp$', HAMP),
	(r'^hamp_new', HAMP_new),
	(r'foreclosure$', foreclosure_probability)
    # Example:
    # (r'^foreclosed/', include('foreclosed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	#(r'^admin/', include(admin.site.urls)),
)
