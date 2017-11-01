from django.contrib import admin
from .models import (
    Artist,
    Album,
    Customer,
    Employee,
    Genre,
    Invoice,
    InvoiceItem,
    Playlist,
    Track
)

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Genre)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Playlist)
admin.site.register(Track)
