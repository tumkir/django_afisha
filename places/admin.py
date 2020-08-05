from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'image_number')

    def get_preview(self, image):
        image = image.image
        return format_html(f'<img src="{image.url}" height=200 />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
