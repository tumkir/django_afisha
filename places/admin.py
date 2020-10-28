from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview', ]
    fields = ['image', 'get_preview', 'image_number']
    extra = 0

    def get_preview(self, image):
        image = image.image
        if image:
            return format_html('<img src="{}" height=200 />', image.url)
        return "Здесь будет превью, когда вы загрузите файл"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
