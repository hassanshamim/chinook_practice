from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import models
from . import serializers


class AlbumList(ListCreateAPIView):
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()

class AlbumDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()

class ArtistList(ListCreateAPIView):
    serializer_class = serializers.ArtistSerializer
    queryset = models.Artist.objects.all()

class ArtistDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ArtistSerializer
    queryset = models.Artist.objects.all()
