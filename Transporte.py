class Transporte:
    def __init__(self, marca, precio, peso_kg):
        self.marca = marca
        self.precio = precio
        self.peso_kg = peso_kg

    def calcular_descuento(self):
        if self.eficiencia in ['A', 'B']:
            return 0.5
        elif self.eficiencia in ['C', 'D']:
            return 0.3
        elif self.eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def calcular_costo_despacho(self, valor_por_kg):
        costo_base_despacho = 4000
        costo_despacho = costo_base_despacho + (self.peso_kg * valor_por_kg)
        return costo_despacho

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca



    def get_eficiencia(self):
        return self.eficiencia

    def set_eficiencia(self, eficiencia):
        self.eficiencia = eficiencia

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_peso_kg(self):
        return self.peso_kg

    def set_peso_kg(self, peso_kg):
        self.peso_kg = peso_kg