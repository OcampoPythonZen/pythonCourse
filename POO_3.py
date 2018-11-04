'''
Clase con Metodo privado, encapsulamos el procedimiento del chequeoInterno el cual solo se llama antes de arranacar el auto
@author: Omar Ocampo
'''
class Coche():
    
    def __init__(self):
        self.LargoChasis=350
        self.AnchoChasis=500
        self.__ruedas=4  		#Esta variable es privada y solo tengo acceso a ella dentro de la clase
        self.__enmarcha=False	#Esta segunda variable la puse privada tambien
             
    def arrancarAuto(self,arrancamos):
        self.__enmarcha=arrancamos
        #Aqui vamos a comprobar el metodo chequeoInterno ya que los carros hacen el chequeo interno antes de poder arrancar
        #lo almacenamos en una variable chequeo el metodo que relizamos de comprobar aceite, gasolina y puertas cerradas
        #y en el segundo if corroboramos el chequeo y encendido (enmarcha)
        if(self.__enmarcha):
        	chequeo=self.__chequeoInterno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en Marcha..."
        elif(self.__enmarcha and chequeo==False):
        	return print("Algo fue mal en el chequeo y no podemos arrancar...")
        else:
            return "Tu auto esta Parado..."
        
    def mostrarEstado(self):
        return print("EL coche tiene", self.__ruedas,"Llantas, Ademas tiene Un ancho de",self.AnchoChasis,"con un largo de",self.LargoChasis)
     
    #Crearemos en esta parte un Metodo privado de la clase que solo sea utilizado para la revisino interna de los autos

    def __chequeoInterno(self):						#se realiza un metodo encapsulado para que no pueda ser modificado y solo utilizado dentro de la clase
    	print("Realizando chequeo de tu auto")
    	
    	self.gasolina="ok"
    	self.aceite="ok"
    	self.puertas="cerradas" 

    	if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
    		return True
    	else:
    		return False

        
obj=Coche()
obj1=Coche()

obj.mostrarEstado()
print(obj.arrancarAuto(True))




print("---- Aqui separamos un objeto de Otro ------")

print(obj1.arrancarAuto(False))
obj1.__ruedas=1
obj1.mostrarEstado()