from Tv import TV
from Scooter import Scooter
from Bicicleta import Bicicleta
from Consola import Consola

class Menu:
    def __init__(self):
        self.productos = []

    def registrar_tv(self):
        marca = input("Ingrese la marca del TV: ")
        voltaje = input("Ingrese el voltaje del TV: ")
        eficiencia = input("Ingrese el nivel de eficiencia del TV (A, B, C, D, E o F): ")
        precio = float(input("Ingrese el precio del TV: "))
        tamaño = input("Ingrese el tamaño del TV: ")
        tv = TV(marca, voltaje, eficiencia, precio, tamaño)
        tv.cotizar()
        self.productos.append(tv)

    def registrar_consola(self):
        marca = input("Ingrese la marca de la Consola: ")
        voltaje = input("Ingrese el voltaje de la Consola: ")
        eficiencia = input("Ingrese el nivel de eficiencia de la Consola (A, B, C, D, E o F): ")
        precio = float(input("Ingrese el precio de la Consola: "))
        nombre = input("Ingrese el nombre de la Consola: ")
        version = input("Ingrese la versión de la Consola (Lite o Normal): ")
        consola = Consola(marca, voltaje, eficiencia, precio, nombre, version)
        consola.cotizar()
        self.productos.append(consola)

    def registrar_scooter(self):
        marca = input("Ingrese la marca del Scooter: ")

        eficiencia = input("Ingrese el nivel de eficiencia del Scooter (A, B, C, D, E o F): ")
        precio = float(input("Ingrese el precio del Scooter: "))
        peso_kg = float(input("Ingrese el peso del Scooter en kg: "))
        aro = input("Ingrese el aro del Scooter: ")
        velocidad = input("Ingrese la velocidad del Scooter: ")
        scooter = Scooter(marca,  eficiencia, precio, peso_kg, aro, velocidad)
        scooter.cotizar()
        self.productos.append(scooter)

    def registrar_bicicleta(self):
        marca = input("Ingrese la marca de la Bicicleta: ")
        precio = float(input("Ingrese el precio de la Bicicleta: "))
        peso_kg = float(input("Ingrese el peso de la Bicicleta en kg: "))
        bicicleta = Bicicleta(marca, precio, peso_kg)
        bicicleta.cotizar()
        self.productos.append(bicicleta)

    def mostrar_productos(self):
        for producto in self.productos:
            if isinstance(producto, TV):
                print("Producto: TV")
            elif isinstance(producto, Consola):
                print("Producto: Consola")
            elif isinstance(producto, Scooter):
                print("Producto: Scooter")
            elif isinstance(producto, Bicicleta):
                print("Producto: Bicicleta")
            producto.mostrar_caracteristicas()


def main():
    menu = Menu()
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Mostrar productos registrados")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            menu.registrar_tv()
        elif opcion == "2":
            menu.registrar_consola()
        elif opcion == "3":
            menu.registrar_scooter()
        elif opcion == "4":
            menu.registrar_bicicleta()
        elif opcion == "5":
            menu.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


main()
