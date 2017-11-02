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

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        fields = '__all__'


class InvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InvoiceItem
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invoice
        fields = '__all__'



class MediaTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MediaType
        fields = '__all__'



class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Track
        fields = '__all__'


class SimpleTrackSerializer(serializers.ModelSerializer):

    album = serializers.StringRelatedField()

    class Meta:
        model = models.Track
        fields = ('id', 'name', 'album')


class PlaylistSerializer(serializers.ModelSerializer):

    total_duration = serializers.SerializerMethodField()
    # tracks = SimpleTrackSerializer(many=True)
    tracks = serializers.StringRelatedField(many=True)


    def get_total_duration(self, obj):
        total_ms =  obj.total_duration
        return '{} seconds'.format(total_ms // 1000)

    class Meta:
        model = models.Playlist
        fields = '__all__'
