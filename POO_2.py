'''
Created on 03/11/2017
Este ejemplo contiene Encapsulacion con la variable ruedas, ya que deseamos que no se modifique
las llantas, ya que si son mas o menos de 4 llantas ya no halamos de un auto. Ejemplfica el uso del
constructor que pasara el valor inicializado a las instancias que se generen de la clase
@author: Omar Ocampo
'''

class Coche():
    
    def __init__(self):
        self.LargoChasis=350
        self.AnchoChasis=500
        self.__ruedas=4
        self.enmarcha=False
        
    def arrancarAuto(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en Marcha..."
        else:
            return "Tu auto esta Parado..."
        
    def mostrarEstado(self):
        return print("EL coche tiene", self.__ruedas,"Llantas, Ademas tiene Un ancho de",self.AnchoChasis,"con un largo de",self.LargoChasis)
        
        
obj=Coche()
obj1=Coche()

print(obj.arrancarAuto(True))
obj.mostrarEstado()
print("---- Aqui separamos un objeto de Otro ------")
print(obj1.enmarcha)
obj1.__ruedas=1
obj1.mostrarEstado()


