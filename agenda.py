#objetivo crear una agenda 
class Personas(object):#crear persona  
	def __init__(self, nombre = "", direccion = "", otra = "" , edad = ""):
		self.nombre = nombre
		self.direccion = direccion
		self.otra = otra
		self.edad = edad

	def __repr__(self):
		return self.nombre+ " "+ self.direccion+ " "+ self.otra+ " "+ self.edad+ \
		"FUNCIONA"


class Preguntador(Personas):
	def __init__(self): #datos 
		self.n1 = raw_input("Dato Nombre 1: ") 
		self.n2 = raw_input("Dato Nombre 2: ")
		self.n3 = raw_input("Dato Nombre 3: ")
		self.n4 = raw_input("Dato Nombre 4: ")

	def poner_nombre(self): 
		
		self.personas = Personas(self.n1, self.n2, self.n3, self.n4)
		return self.personas


	def lo_en_listo(self, lista_out):#lista con los datos 
		self.lista_out = lista_out 
		self.poner_nombre_estenombre = self.poner_nombre()
		self.lista_llena = self.lista_out.append(self.poner_nombre_estenombre)
		return self.lista_llena
	

listaDeClases = []
while True:

	listaId = [1, 2, 3] #AGREGAR ID  

	for i in range(0, 3): 
		listaId[i] = Preguntador()#listas 
		listaId[i].lo_en_listo(listaDeClases)#Pon las listas ya creadas en la lista principal


	print listaDeClases #Muestra las listas 
	
	salir = raw_input("Quieres salir y/n: ")
	if salir == "y":
		break
	else:
		pass

for i in listaDeClases:
	for a in i:
		print listaDeClases[i][a]	
