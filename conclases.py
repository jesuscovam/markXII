class Acuaticas:
	def __init__(self, nombre):
		self.nombre = nombre

class Culturales:
	def __init__(self, nombre):
		self.nombre = nombre

class Culinarias:
	def __init__(self, nombre):
		self.nombre = nombre

class Extremas:
	def __init__(self, nombre):
		self.nombre = nombre

#Encabezado
experiencias = ['Acuaticas', 'Culturales', 'Culinarias', 'Extremas']

#Acuaticas
xelha = Acuaticas('Xel-Ha')
ruta = Acuaticas('Ruta de Cenotes')
cozumel = Acuaticas('Cozumel')
kantun = Acuaticas('Cenote Kanun Chi')
acuaticask = [xelha, ruta, cozumel, kantun]

#Culturales
xcaret = Culturales('Xcaret')
quinta = Culturales('5ta Avenida')
museo = Culturales('Museo de Frida Kahlo')
plaza = Culturales('Plaza en la Playa')
culturalesk = [xcaret, quinta, museo, plaza]

#Culinarias
fogon = Culinarias('El Fogón')
mu = Culinarias('Mu BurgerHouse')
orange = Culinarias('Café Orange')
parrilla = Culinarias('La Parrilla')
culinariask = [fogon, mu, orange, parrilla]

#Extremas
xplor = Extremas('Xplor')
rio = Extremas('Río Secreto')
kantun = Extremas('Cenote Kantun Chin')
buceo = Extremas('Buceo en Cozumel')
extremask = [xplor, rio, kantun, buceo]

#Mensajes
mensajes = {'inicio': 'Escoja su primera experiencia: ',
							'desarrollo': 'Siguiente: ',
							'final': 'Por Último: ',
							'gracias': '¡Gracias!',
							'cuantico': 'Escoja una de las siguientes: ',
							'generales': 'Estas son nuestras experiencias generales',
							'especificas': 'Estas son nuestras experiencias especificas'}
#LOOPS
#Encabezados
def entradas():
	print(mensajes['generales'])
	i= 1
	for x in experiencias:
		o = str(i) + ': '
		print(x)
		i = i + 1

#Especificos
def especificos(tema):
	print(mensajes['especificas'])
	i = 1
	for x in tema:
		o = str(i) + ': '
		print(o + x.nombre)
		i = i + 1


#Variables
tour = []
eleccion = []

#CONDICIONALES
#general
def con_general(entrada):
	if entrada == 1:
		especificos(acuaticask)
		micro(entrada, acuaticask)
	elif entrada ==2:
		especificos(culturalesk)
		micro(entrada, culturalesk)
	elif entrada ==3:
		especificos(culinariask)
		micro(entrada, culinariask)
	else:
		especificos(extremask)
		micro(entrada, extremask)

#especifico
def agregar_exp(entrada, tema):
	global tour
	tour.append(tema[entrada])

#INPUTS
def macro():
	pregunta = int(input(mensajes[inicio]))

def micro(entrada, tema):
	pregunta = int(input(mensajes[cuantico]))
	agregar_exp(entrada, tema)


#INTERFAZ

#Inicio
def aplicacion():
	entradas()





aplicacion()
