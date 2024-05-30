"""no es el codigo equivalente a la de la entrega del workshop 1 solo es una correccion la del workshop1 es la version anterior"""

class Motor:
    """Clase Motor que contiene los atributos de un motor."""
    def __init__(self, nombre, tipo_motor: str, potencia_motor: int, peso: float):
        self.nombre_ = nombre
        self.tipo_motor_ = tipo_motor
        self.potencia_motor_ = potencia_motor
        self.peso_ = peso

class Vehiculo:
    """Clase Vehículo que contiene los atributos de un vehículo y su consumo de gasolina."""
    def __init__(self, chasis: str, modelo: str, year: int, motor):
        self.chasis_ = chasis
        self.modelo_ = modelo
        self.year_= year
        self.consumo_de_gas_ = None
        self.motor_ = motor
        valor_chasis_ = 0
        if chasis == "A":
            valor_chasis_ = 0.5
        elif chasis == "B":
            valor_chasis_ = 0.3
        else:
            print("Ingrese un valor correcto para el chasis")

        # pylint: disable=line-too-long
        self.consumo_de_gas_ = ((1.1 * (self.motor_.potencia_motor_ if self.motor_.potencia_motor_ > 0 else 0)) +
                                (0.2 * (self.motor_.peso_ if self.motor_.peso_ > 0 else 0)) - (valor_chasis_))
        print(f"Consumo de gasolina del vehículo {self.modelo_}: {self.consumo_de_gas_:.2f} litros/km")

class Carrito(Vehiculo):
    """Clase Carrito que hereda de la clase Vehículo y contiene los atributos de un carrito."""
    def __str__(self):
        return f"Carrito - Modelo: {self.modelo_}, Año: {self.year_}, Chasis: {self.chasis_}"

class Tractor(Vehiculo):
    """Clase Tractor que hereda de la clase Vehículo y contiene los atributos de un tractor."""
    def __str__(self):
        return f"Tractor - Modelo: {self.modelo_}, Año: {self.year_}, Chasis: {self.chasis_}"

class Camion(Vehiculo):
    """Clase Camión que hereda de la clase Vehículo y contiene los atributos de un camión."""
    def __str__(self):
        return f"Camión - Modelo: {self.modelo_}, Año: {self.year_}, Chasis: {self.chasis_}"

class Yate(Vehiculo):
    """Clase Yate que hereda de la clase Vehículo y contiene los atributos de un yate."""
    def __str__(self):
        return f"Yate - Modelo: {self.modelo_}, Año: {self.year_}, Chasis: {self.chasis_}"

class Moto(Vehiculo):
    """Clase Moto que hereda de la clase Vehículo y contiene los atributos de una moto."""
    def __str__(self):
        return f"Moto - Modelo: {self.modelo_}, Año: {self.year_}, Chasis: {self.chasis_}"

# pylint: disable=global-at-module-level
global vehiculos
vehiculos = []

# pylint: disable=global-at-module-level
global motores
motores = []

def crear_motor():
    """Función que crea un motor y lo añade a la lista de motores."""
    print("Ingrese el nombre del motor:")
    nombre = input()
    print("Ingrese que tipo de motor es:")
    tipo_motor = input()
    print("Ingrese la potencia del motor:")
    potencia_motor = int(input())
    print("Ingrese el peso del motor:")
    peso = float(input())
    motor_nuevo = Motor(nombre, tipo_motor, potencia_motor, peso)
    motores.append(motor_nuevo)
    print("Motor creado con éxito.")

def crear_vehiculo(vehiculo):
    """Función que crea un vehículo y lo añade a la lista de vehículos."""
    if not motores:
        print("Debe crear al menos un motor primero.")
        return

    print("Seleccione un motor para el vehículo:")
    for i, motor in enumerate(motores):
        print(f"{i+1}. {motor.nombre_}")

    seleccion = int(input("Ingrese el número del motor seleccionado: ")) - 1

    if seleccion < 0 or seleccion >= len(motores):
        print("Selección inválida.")
        return

    motor_seleccionado = motores[seleccion]

    print("Ingrese el modelo del vehículo:")
    modelo = input()
    print("Ingrese el año del modelo del vehículo:")
    year = int(input())
    print("Ingrese el chasis que va a tener su vehículo (Elija entre chasis A o B):")
    chasis = input()
    print("El consumo de gasolina sería el siguiente:")

    if vehiculo == "Carrito":
        vehiculos.append(Carrito(chasis, modelo, year, motor_seleccionado))
    elif vehiculo == "Tractor":
        vehiculos.append(Tractor(chasis, modelo, year, motor_seleccionado))
    elif vehiculo == "Camión":
        vehiculos.append(Camion(chasis, modelo, year, motor_seleccionado))
    elif vehiculo == "Yate":
        vehiculos.append(Yate(chasis, modelo, year, motor_seleccionado))
    elif vehiculo == "Moto":
        vehiculos.append(Moto(chasis, modelo, year, motor_seleccionado))

def menu():
    """Función que muestra el menú de opciones."""
    while True:
        print("MENU")
        print("1. Crear un motor")
        print("2. Crear un carro")
        print("3. Crear un tractor")
        print("4. Crear un camión")
        print("5. Crear un yate")
        print("6. Crear una moto")
        print("7. Ver lista de motores")
        print("8. Ver todos los vehículos")
        print("9. Salir")

        x = int(input("Seleccione una opción: "))
        if x == 1:
            crear_motor()
        elif x == 2:
            crear_vehiculo("Carrito")
        elif x == 3:
            crear_vehiculo("Tractor")
        elif x == 4:
            crear_vehiculo("Camión")
        elif x == 5:
            crear_vehiculo("Yate")
        elif x == 6:
            crear_vehiculo("Moto")
        elif x == 7:
            for i, motor in enumerate(motores):
                print(f"{i+1}. {motor.nombre_}")
        elif x == 8:
            for vehiculo in vehiculos:
                print(vehiculo)
        elif x == 9:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
