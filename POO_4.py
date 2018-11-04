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


#Heredamos de clase Vehiculo
class Moto(vehiculo):
		#pass	#pass se usa para no hacer nada y cumplir con la sintaxis, en este caso pasa primero el constructor y las funciones
	hcaballito="Levantando una llanta"

	def caballito(self):
		return print(self.hcaballito)

	def estado(self):	#Cuando creamos un metodo con el mismo nombre lo sobreescribe de la clase padre.
		return print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.enmarcha,"\nAcelera:",self.acelera,"\nFrenado:",self.frena,"\nCaballo?:",self.hcaballito)
#-------------------------------------
class Furgoneta(vehiculo):
	pass



miMoto=Moto("Suzuki","GIXXER")
miMoto.estado()
print('\n')
miFurgo=Furgoneta("BAJAJ","Pulsar 200")
miFurgo.estado()