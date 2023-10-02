from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, marca, precio, peso_kg):
        super().__init__(marca, precio, peso_kg)

    def cotizar(self):
        costo_despacho = self.calcular_costo_despacho(400)
        precio_con_descuento = self.precio
        valor_total = precio_con_descuento + costo_despacho
        print("Características de Bicicleta:")
        print("Marca:", self.marca)
        print("Costo del despacho:", costo_despacho)
        print("Valor total luego del despacho:", valor_total)

    def mostrar_caracteristicas(self):
        print("Características de Bicicleta:")
        print("Marca:", self.marca)
        print("Peso en kg:", self.peso_kg)

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_peso_kg(self):
        return self.peso_kg

    def set_peso_kg(self, peso_kg):
        self.peso_kg = peso_kg

