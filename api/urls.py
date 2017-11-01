from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'album/$', views.AlbumList.as_view(), name='album-list'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-list'),

    url(r'artist/$', views.ArtistList.as_view(), name='artist-list'),
    url(r'artist/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view(), name='artist-list'),

    url(r'customer/$', views.CustomerList.as_view(), name='customer-list'),
    url(r'customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view(), name='customer-list'),

    url(r'employee/$', views.EmployeeList.as_view(), name='employee-list'),
    url(r'employee/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name='employee-list'),

    url(r'genre/$', views.GenreList.as_view(), name='genre-list'),
    url(r'genre/(?P<pk>[0-9]+)/$', views.GenreDetail.as_view(), name='genre-list'),


    # url(r'xx/$', views.XXList.as_view(), name='xx-list'),
    # url(r'xx/(?P<pk>[0-9]+)/$', views.XXDetail.as_view(), name='xx-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

