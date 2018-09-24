def lado():
    global lado
    lado = int(input("Introduzca el valor del lado del cuadrado: "))

def area_cuadrado():
   print("El área del cuadrado es", lado*lado)

lado()
area_cuadrado()