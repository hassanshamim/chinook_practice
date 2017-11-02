from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics

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


class CustomerList(ListCreateAPIView):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()


class EmployeeList(ListCreateAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class GenreList(ListCreateAPIView):
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()


class GenreDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()


class InvoiceList(ListCreateAPIView):
    serializer_class = serializers.InvoiceSerializer
    queryset = models.Invoice.objects.all()


class InvoiceDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.InvoiceSerializer
    queryset = models.Invoice.objects.all()


class MediaTypeList(generics.CreateAPIView):
    serializer_class = serializers.MediaTypeSerializer
    queryset = models.MediaType.objects.all()


class MediaTypeDetail(generics.RetrieveAPIView):
    serializer_class = serializers.MediaTypeSerializer
    queryset = models.MediaType.objects.all()


class PlaylistList(ListCreateAPIView):
    serializer_class = serializers.PlaylistSerializer
    queryset = models.Playlist.objects.all()


class PlaylistDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PlaylistSerializer
    queryset = models.Playlist.objects.select_related().all()

class TrackList(ListCreateAPIView):
    serializer_class = serializers.TrackSerializer
    queryset = models.Track.objects.all()


class TrackDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TrackSerializer
    queryset = models.Track.objects.all()