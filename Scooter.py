from Transporte import Transporte
class Scooter(Transporte):
    def __init__(self, marca,  eficiencia, precio, peso_kg, aro, velocidad):
        super().__init__(marca, eficiencia, precio, peso_kg)
        self.aro = aro
        self.velocidad = velocidad

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        costo_despacho = self.calcular_costo_despacho(300)
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        valor_total = precio_con_descuento + costo_despacho
        print("Características de Scooter:")
        print("Marca:", self.marca)
        
        print("Eficiencia:", self.eficiencia)
        print("Aro:", self.aro)
        print("Velocidad:", self.velocidad)
        print("Descuento aplicado:", descuento_eficiencia * 100, "%")
        print("Costo del despacho:", costo_despacho)
        print("Valor total luego del descuento y despacho:", valor_total)

    def mostrar_caracteristicas(self):
        print("Características de Scooter:")
        print("Marca:", self.marca)
       
        print("Eficiencia:", self.eficiencia)
        print("Aro:", self.aro)
        print("Velocidad:", self.velocidad)
        print("Peso en kg:", self.peso_kg)

    def get_aro(self):
        return self.aro

    def set_aro(self, aro):
        self.aro = aro

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad