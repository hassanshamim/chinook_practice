from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'album/$', views.AlbumList.as_view(), name='album-list'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-list'),
    url(r'artist/$', views.ArtistList.as_view(), name='artist-list'),
    url(r'artist/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view(), name='artist-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

