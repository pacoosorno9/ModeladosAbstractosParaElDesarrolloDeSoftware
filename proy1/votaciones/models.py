import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_publicacion = models.DateField("Fecha de publicacion de la pregunta")

    def __str__(self):
        return self.texto_pregunta

    def fue_publicado_recientemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.fecha_publicacion <= now
        # return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):

    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_respuesta