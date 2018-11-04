class persona():
	"""docstring for persona"""
	def __init__(self,nombre,edad,lugar_res):
		self.nombre=nombre
		self.edad=edad
		self.lugar_res=lugar_res

	def descripcion(self):
		return print("Nombre:",self.nombre,"Edad:",self.edad,"Lugar de Residencia:",self.lugar_res)

class empleado(persona):
	def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,lugar_res_empleado):
		super().__init__(nombre_empleado,edad_empleado,lugar_res_empleado)
		self.salario=salario
		self.antiguedad=antiguedad

		#Reescribo la funcion padre de persona
	def descripcion(self):
		super().descripcion()
		print("Salario $",self.salario,"Años de Antiguedad",self.antiguedad)

		#funcion super() llama al metodo __init__ de la clase padre dandole los parametros que usa su constructor __init__

instEmpleado=empleado(120000,15,'Edgar',31,'Edo.Mex')
print(isinstance(instEmpleado,persona))
instEmpleado.descripcion()




