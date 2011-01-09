from django.conf.urls.defaults import *
from views import index
from foreclosure_probability.foreclosure_probability import foreclosure_probability
from lead_gen.lead_gen import lead_gen_display

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),
	(r'^foreclosed$', index),
	#(r'administrate', administrate),
	(r'foreclosure$', foreclosure_probability),
	(r'lead_gen_leads$', lead_gen_display)
    # Example:
    # (r'^foreclosed/', include('foreclosed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	#(r'^admin/', include(admin.site.urls)),
)
