from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'album/$', views.AlbumList.as_view(), name='album-list'),
    url(r'album/(?P<pk>[0-9]+)/$',
        views.AlbumDetail.as_view(),
        name='album-list'),


    url(r'artist/$', views.ArtistList.as_view(), name='artist-list'),
    url(r'artist/(?P<pk>[0-9]+)/$',
        views.ArtistDetail.as_view(),
        name='artist-list'),


    url(r'customer/$', views.CustomerList.as_view(), name='customer-list'),
    url(r'customer/(?P<pk>[0-9]+)/$',
        views.CustomerDetail.as_view(),
        name='customer-list'),


    url(r'employee/$', views.EmployeeList.as_view(), name='employee-list'),
    url(r'employee/(?P<pk>[0-9]+)/$',
        views.EmployeeDetail.as_view(),
        name='employee-list'),


    url(r'genre/$', views.GenreList.as_view(), name='genre-list'),
    url(r'genre/(?P<pk>[0-9]+)/$',
        views.GenreDetail.as_view(),
        name='genre-list'),


    url(r'invoice/$', views.InvoiceList.as_view(), name='invoice-list'),
    url(r'invoice/(?P<pk>[0-9]+)/$',
        views.InvoiceDetail.as_view(),
        name='invoice-list'),


    url(r'media_type/$', views.MediaTypeList.as_view(), name='media_type-list'),
    # url(r'media_type/(?P<pk>[0-9]+)/$', views.MediaTypeDetail.as_view(), name='media_type-list'),


    url(r'playlist/$', views.PlaylistList.as_view(), name='playlist-list'),
    url(r'playlist/(?P<pk>[0-9]+)/$',
        views.PlaylistDetail.as_view(),
        name='playlist-list'),


    url(r'track/$', views.TrackList.as_view(), name='track-list'),
    url(r'track/(?P<pk>[0-9]+)/$',
        views.TrackDetail.as_view(),
        name='track-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
