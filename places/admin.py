from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_number', 'place', 'image')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
