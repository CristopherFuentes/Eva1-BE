from Tecnologia import Tecnologia


class Consola(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.nombre = nombre
        self.version = version

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        if "Lite" in self.version:
            descuento_adicional = 0.05
        else:
            descuento_adicional = 0

        descuento_total = descuento_eficiencia + descuento_adicional
        precio_con_descuento = self.precio * (1 - descuento_total)
        print("Características de Consola:")
        self.mostrar_caracteristicas()
        print("Nombre:", self.nombre)
        print("Versión:", self.version)
        print("Descuento aplicado (eficiencia):", descuento_eficiencia * 100, "%")
        print("Descuento aplicado (versión Lite):", descuento_adicional * 100, "%")
        print("Valor total luego del descuento:", precio_con_descuento)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version