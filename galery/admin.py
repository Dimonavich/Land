from django.contrib import admin
from galery.models import Imagenes


class ImagenesAdmin(admin.ModelAdmin):

    list_filter = ['Imagenes_data', 'Imagenes_name', 'Imagenes_url']

admin.site.register(Imagenes, ImagenesAdmin)