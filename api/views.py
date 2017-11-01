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