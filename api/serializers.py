from rest_framework import serializers

from . import models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = '__all__'

class SimpleAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Album
        exclude = ('artist',)

class ArtistSerializer(serializers.ModelSerializer):

    albums = SimpleAlbumSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Artist
        fields = ('id', 'name', 'albums')

