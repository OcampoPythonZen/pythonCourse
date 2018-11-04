import datetime

class calculo_fechas():

    def __init__(self,fecha_inicial,fecha_final):
        self.fecha_inicial=fecha_inicial
        self.fecha_final=fecha_final

    def diferencia_dias(self):
        return fecha_final-fecha_inicial
