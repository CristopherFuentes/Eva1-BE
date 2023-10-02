from Tecnologia import Tecnologia

class TV(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamaño):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.tamaño = tamaño

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        print("Características de TV:")
        self.mostrar_caracteristicas()
        print("Tamaño:", self.tamaño)
        print("Descuento aplicado:", descuento_eficiencia * 100, "%")
        print("Valor total luego del descuento:", precio_con_descuento)

    def get_tamaño(self):
        return self.tamaño

    def set_tamaño(self, tamaño):
        self.tamaño = tamaño

