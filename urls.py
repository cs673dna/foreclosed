from django.conf.urls.defaults import *
<<<<<<< HEAD
from views import index, HAMPResults, administrate
=======
from views import index, HAMP
>>>>>>> f80be83dfb0aa8f48c1fe45dfed72ba0f4782047

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),
<<<<<<< HEAD
	(r'hamp', HAMPResults),
	(r'administrate', administrate),
=======
	(r'^hamp$', HAMP)
>>>>>>> f80be83dfb0aa8f48c1fe45dfed72ba0f4782047
    # Example:
    # (r'^foreclosed/', include('foreclosed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	#(r'^admin/', include(admin.site.urls)),
)
