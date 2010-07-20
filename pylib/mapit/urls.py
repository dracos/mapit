from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^postcode/(?P<postcode>[A-Za-z0-9 ]+)$', 'mapit.postcodes.views.postcode'),
    (r'^area/(?P<area_id>[0-9]+)$', 'mapit.areas.views.area'),
    (r'^admin/', include(admin.site.urls)),

    # Old style calls
    (r'^get_voting_areas/([A-Za-z0-9 ]+)$', 'mapit.postcodes.views.get_voting_areas'),
    (r'^get_voting_area_info$', 'mapit.areas.views.get_voting_area_info'),
    (r'^get_voting_areas_info$', 'mapit.areas.views.get_voting_areas_info'),
    (r'^get_voting_area_by_name$', 'mapit.areas.views.get_voting_area_by_name'),
    (r'^get_areas_by_type$', 'mapit.areas.views.get_areas_by_type'),
    (r'^get_voting_area_geometry$', 'mapit.areas.views.get_voting_area_geometry'),
    (r'^get_voting_areas_geometry$', 'mapit.areas.views.get_voting_areas_geometry'),
    (r'^get_voting_areas_by_location$', 'mapit.areas.views.get_voting_areas_by_location'),
    (r'^get_example_postcode/([0-9]+)$', 'mapit.postcodes.views.get_example_postcode'),
    (r'^get_voting_area_children$', 'mapit.areas.views.get_voting_area_children'),
    (r'^get_location/([A-Za-z0-9 ]+)(?:/(partial))?$', 'mapit.postcodes.views.get_location'),
    (r'^get_location$', 'mapit.postcodes.views.get_location'),
)
