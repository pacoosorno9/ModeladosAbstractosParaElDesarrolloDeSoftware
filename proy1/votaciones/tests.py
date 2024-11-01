import datetime

from django.test import TestCase
from django.utils import timezone
from django.test import TestCase

from .models import Pregunta

# Create your tests here.
class PreguntaModelTest(TestCase):
    def test_fue_publicado_recientemente_con_futuro(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futuro = Pregunta(fecha_publicacion=time)
        self.assertIs(futuro.fue_publicado_recientemente(), False)

    def test_fue_publicaco_recientementey_cpn_pregunta_vieja(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old = Pregunta(fecha_publicacion=time)
        self.assertIs(old.fue_publicado_recientemente(), False)


    def test_fue_publicaco_recientemente_con_reciente_pregunta(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        reciente = Pregunta(fecha_publicacion=time)
        self.assertIs(reciente.fue_publicado_recientemente(), True)
