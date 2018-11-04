class Coche():

	largo_chasis=350
	ancho_chasis=250
	ruedas=4
	quema_coco=False
	en_marcha=False

	# def __init__(self): Este es el contructor de mi clase
	# toma los valores que se definen cuandose lleva acabo una instancia de la clase
		
	# 	self.largo_chasis=350
	# 	self.ancho_chasis=250
	# 	self.ruedas=4
	# 	self.quema_coco=False
	# 	self.en_marcha=False

	def arrancar(self):
		self.en_marcha=True
		return print("Encendiendo la marcha de tu coche...")

	def ver_estado(self):
		if (self.en_marcha):
			return "En Marcha."
		else:	
			return "Sin Marcha."

mc=Coche()
mc1=Coche()

print("Tu Carro contiene",mc.ruedas,"llantas","ademas las medidas son:",mc.largo_chasis,"por",mc.ancho_chasis,"Tiene QuemaCoco?",mc.quema_coco)
print("El estado de tu Carro_1 es:",mc.ver_estado())
print("------ Aqui se separa la segunda instancia de Coche -------")

mc1.ruedas=1

print("Tu Carro contiene",mc1.ruedas,"llantas","ademas las medidas son:",mc1.largo_chasis,"por",mc1.ancho_chasis,"Tiene QuemaCoco?",mc1.quema_coco)
print("El estado de tu Carro_2 es:",mc1.ver_estado())
mc1.arrancar()
print("El estado de tu Carro_2 es:",mc1.ver_estado())