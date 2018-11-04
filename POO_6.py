class vehiculo():

	def __init__(self,marca,modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		return print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelera:",self.acelera,"\nFrenado:",self.frena)

#Algo que no podia hacer en Java era declarar varias clases de manera normal en el mismo .java Aqui se denota como solo se declaran sin alguna otra
#palabra reservada

class Furgoneta(vehiculo):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return print("La Furgoneta esta cargada...")
		else:
			return print('No esta cargada tu Furgoneta')

#Heredamos de clase Vehiculo
class Moto(vehiculo):
		#pass	#pass se usa para no hacer nada y cumplir con la sintaxis, en este caso pasa primero el constructor y las funciones
	hcaballito="Levantando una llanta"

	def caballito(self):
		return print(self.hcaballito)

	def estado(self):	#Cuando creamos un metodo con el mismo nombre lo sobreescribe de la clase padre.
		return print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelera:",self.acelera,"\nFrenado:",self.frena,"\nCaballo?:",self.hcaballito)

class Velectricos():
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100
	def cargarEnergia(self):
		self.cargando=True
	def estado(self):
		return print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelera:",self.acelera,"\nFrenado:",self.frena,"\nAutonomia:",self.autonomia)

class biciElectrica(Velectricos,vehiculo):
	pass									    #hacemos herencia multiple separadas por como se ponen las clases y hereda todas las propiedades de ambas clases
												#se le da preferencia a la primera clase que Indiques en este caso fue a Velectricos

miMoto=Moto("Suzuki","GIXXER")
miMoto.estado()
print('\n')
miFurgoneta=Furgoneta("Suzuki","CBR750")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)
print('\n')
miBici=biciElectrica("Spark","chevrolet")
miBici.estado()
