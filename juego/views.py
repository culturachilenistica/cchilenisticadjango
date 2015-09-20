from django.shortcuts import render
from .models import Pregunta
import demjson

def inicio(request):
	html = "<html><body>Hola Mundo desde DJANGO</body></html>"
	return render(request, 'juego/inicio.html',{})

def empezar_juego(request):
	diez_preguntas = Pregunta.objects.all();
	#todas_categorias = Categoria.objects.all();
	texto= [diez_preguntas[0].texto_pregunta,diez_preguntas[1].texto_pregunta];
	alternativas1= [diez_preguntas[0].alternativa_1,diez_preguntas[1].alternativa_1];
	alternativas2= [diez_preguntas[0].alternativa_2,diez_preguntas[1].alternativa_2];
	alternativas3= [diez_preguntas[0].alternativa_3,diez_preguntas[1].alternativa_3];
	alternativas4= [diez_preguntas[0].alternativa_4,diez_preguntas[1].alternativa_4];
	ruta_imagen  = [diez_preguntas[0].ruta_imagen,diez_preguntas[1].ruta_imagen];
	a_correctas =  [diez_preguntas[0].alternativa_correcta,diez_preguntas[1].alternativa_correcta];
	#categorias = [todas_categorias[0]]

	data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

	json = demjson.encode(data)
	print json

	return render(request, 'juego/juego.html',{
		'pregunta1':texto[0],
		'pregunta2':texto[1],
		'alternativa1_1':alternativas1[0],
		'alternativa1_2':alternativas1[1],
		'alternativa2_1':alternativas2[0],
		'alternativa2_2':alternativas2[1],
		'alternativa3_1':alternativas3[0],
		'alternativa3_2':alternativas3[1],
		'alternativa4_1':alternativas4[0],
		'alternativa4_2':alternativas4[1],
		'ruta_imagen_1':ruta_imagen[0],
		'ruta_imagen_2':ruta_imagen[1],
		'a_correcta_1':a_correctas[0],
		'a_correcta_2':a_correctas[1],
		})

