# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    id = models.AutoField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase. This field type is a guess.
    artist = models.ForeignKey('Artist',
        db_column='ArtistId',
        related_name='albums',
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = 'albums'

    def __str__(self):
        return self.title


class Artist(models.Model):
    id = models.AutoField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'artists'

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.AutoField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    support_rep = models.ForeignKey('Employee',
        db_column='SupportRepId',
        blank=True,
        null=True,
        related_name='customers',
        on_delete=models.SET_NULL)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class Employee(models.Model):
    id = models.AutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    manager = models.ForeignKey('self',
        db_column='ReportsTo',
        on_delete=models.SET_NULL,
        related_name='subordinates',
        null=True,
        blank=True,
    )

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class Genre(models.Model):
    id = models.AutoField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'genres'

    def __str__(self):
        return self.name


class InvoiceItem(models.Model):
    id = models.AutoField(db_column='InvoiceLineId', primary_key=True)  # Field name made lowercase.
    invoice = models.ForeignKey('Invoice', db_column='InvoiceId', on_delete=models.CASCADE)  # Field name made lowercase.
    track = models.ForeignKey('Track', db_column='TrackId', on_delete=models.CASCADE)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice',
        decimal_places=2,
        max_digits=6
    )  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_items'


class Invoice(models.Model):
    id = models.AutoField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    billingaddress = models.TextField(db_column='BillingAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingcity = models.TextField(db_column='BillingCity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingstate = models.TextField(db_column='BillingState', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingcountry = models.TextField(db_column='BillingCountry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total = models.DecimalField(db_column='Total',
        decimal_places=2,
        max_digits=6,
    )  # Field name made lowercase. This field type is a guess.

    customer = models.ForeignKey(
        Customer,
        db_column='CustomerId',
        related_name='invoices',
        on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoices'

    def __str__(self):
        return 'Invoice #%s for: %s' % (self.id, self.customer)


class MediaType(models.Model):
    id = models.AutoField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media_types'

    def __str__(self):
        return self.name


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey('Playlist',
        db_column='PlaylistId',
        on_delete=models.CASCADE,
    )  # Field name made lowercase.
    track = models.ForeignKey('Track',
        db_column='TrackId',
        on_delete=models.CASCADE,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist_track'
        unique_together = (('playlist', 'track'),)


class Playlist(models.Model):
    playlist = models.AutoField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tracks = models.ManyToManyField('Track',
        related_name='playlists',
        through=PlaylistTrack,
    )

    class Meta:
        managed = False
        db_table = 'playlists'

    def __str__(self):
        return self.name


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Track(models.Model):
    id = models.AutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    composer = models.TextField(db_column='Composer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice',
        max_digits=6,
        decimal_places=2
    )  # Field name made lowercase. This field type is a guess.

    album = models.ForeignKey(Album,
        db_column='AlbumId',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='tracks'
    )
    media_type = models.ForeignKey(MediaType,
        db_column='MediaTypeId',
        related_name='tracks',
        on_delete=models.CASCADE,
    )
    genreid = models.ForeignKey(Genre,
        db_column='GenreId',
        blank=True,
        null=True,
        related_name='tracks',
        on_delete=models.SET_NULL
      )

    class Meta:
        managed = False
        db_table = 'tracks'

    def __str__(self):
        return self.name
