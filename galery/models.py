from django.db import models


class Imagenes(models.Model):
    class Meta():
        db_table = "Imagenes"
    Imagenes_url = models.URLField()
    Imagenes_name = models.CharField(max_length=200)
    Imagenes_data = models.DateTimeField()


