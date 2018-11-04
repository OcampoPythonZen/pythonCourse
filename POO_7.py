class Coche():
	def desplaza(self):
		print('EL coche tiene 4 llantas')

class Moto():
	def desplaza(self):
		print('La moto tiene 2 llantas')

class Camion():
	def desplaza(self):
		print('El camión tiene 6 llantas')

#Si generamos una instacia de cualquer clase nos arroja el mensaje de cada instancia creada
#¿Pero? que sucede si realizamos una fucion que pase como parametro un objeto llamado vehiculo
#Este objeto como parametro llama a su vez a la funcion desplaza() ¿A CUAL DE LAS # FUNCIONES LLAMA?

def desplazaVehiculo(vehiculo):
	vehiculo.desplaza()
#La magia del polimofismo sucede cuando pueda tomar el comportamiento de cualquier deplaza() de cualquier clase
#Creamos una instancia  de camion y vemos como se comportara
instanciaCamion=Camion()
desplazaVehiculo(instanciaCamion)
#Si hacemos lo mismo con otra instancia de clase veremos que puedo tomar el comportamiento de la funcion de la clase
#que se le pasa por el parametro de objeto
instanciaMoto=Moto()
desplazaVehiculo(instanciaMoto)
