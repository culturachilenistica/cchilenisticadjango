from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Partida(models.Model):
    id_partida = models.AutoField(primary_key=True)
    #usuario = models.ForeignKey('auth.Jugador')
    cantidad_correctas = models.PositiveSmallIntegerField(blank=False,
        null=False,default=0)
    cantidad_incorrectas = models.PositiveSmallIntegerField(blank=False,
        null=False,default=0)
    cantidad_omitidas = models.PositiveSmallIntegerField(blank=False,
        null=False,default=0)
    puntaje_obtenido = models.IntegerField(blank=False,
        null=False,default=0,editable=False)
    fecha_creacion = models.DateTimeField(
        default=timezone.now, editable=False,
        blank=True, null=True)
    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()

class Partida_Preguntas(models.Model):
    id_partida_pregunta = models.AutoField(primary_key=True)
    partida = models.ForeignKey('juego.Partida')
    pregunta = models.ForeignKey('juego.Pregunta')

class Categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	nombre_categoria = models.CharField(max_length=50,
		null = False, blank = False,
		default = 'General')
	fecha_creacion = models.DateTimeField(
    	default=timezone.now, editable=False,
    	blank=True, null=True)

	def __str__(self):
		return self.nombre_categoria

	def publish(self):
		self.fecha_creacion = timezone.now()
		self.save()


class Pregunta(models.Model):
    #author = models.ForeignKey('auth.User')
    #pregunta = models.CharField(max_length=200)#Texto largo definido
    #title = models.CharField(max_length=200)
    categoria = models.ForeignKey('juego.Categoria',default=1)
    id_pregunta = models.AutoField(primary_key=True)
    texto_pregunta = models.TextField(null=True,blank=False,
    	default = 'No existe texto en el campo pregunta')
    alternativa_1 = models.CharField(max_length=500,default='Alternativa 1',
    	blank=False,null=False)#Largo sin definir
    alternativa_2 = models.CharField(max_length=500,default='Alternativa 2',
    	blank=False)
    alternativa_3 = models.CharField(max_length=500,default='Alternativa 3',
    	blank=False)
    alternativa_4 = models.CharField(max_length=500,default='Alternativa 4',
    	blank=False)
    alternativa_correcta_choices = (
    	(1,'Alternativa 1'),
    	(2,'Alternativa 2'),
    	(3,'Alternativa 3'),
    	(4,'Alternativa 4'),
    )
    alternativa_correcta = models.PositiveSmallIntegerField(
    	choices = alternativa_correcta_choices,
    	default = 1,blank=False,null=False)

    ruta_imagen = models.CharField(max_length=140,
        default="")

    fecha_creacion = models.DateTimeField(
        default=timezone.now, editable=False,
        blank=False, null=True)

    def __str__(self):
       return self.texto_pregunta

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()