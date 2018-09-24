'''
Created on 04/09/2018

@author: David Barocio
'''
import sys

#Función para capturar el radio del círculo
def val_radio():
   global radio
   radio = float(input("Introduce el radio: "))

#Función para calcular el pi del círculo
def val_pi():
   global pi
   pi = float(3.141592654)

#Función para capturar la base
def base():
   global base
   base = int(input("Escriba la base a calcular: "))

#Función para capturar la altura
def altura():
    global altura
    altura = int(input("Escriba la altura a calcular: "))

#Función para capturar el lado
def lado():
    global lado
    lado = int(input("Introduzca el valor del lado del cuadrado: "))

#Función para calcular el área de un cuadrado
def area_cuadrado():
   print("El área del cuadrado es", lado*lado)

#Función para calcular el área de un triángulo
def area_triangulo():
        print("El área del triángulo es: ", base*altura/2)

#Función para calcular el área de un círculo
def area_circulo():
    if radio >= 0:
        print("El área del círculo es: ", round(pi * radio**2,3))
    else:
        print("El radio no es correcto")

print("Selecciona la operación a realizar: ")
'''
#Función para continuar o salir
def salida():
    sys.exit()
'''

#Menú de la calculadora
respuesta="si"
while respuesta != "no":
    print("1 - Calcular el área de un cuadrado")
    print("2 - Calcular el área de un triángulo")
    print("3 - Calcular el área de un círculo")
    print("4 - Salir")
    operacion = int(input("Introduce el número de operación a realizar: "))
    if (operacion == 1):
        lado()
        area_cuadrado()
    elif(operacion == 2):
        base()
        altura()
        area_triangulo()
    elif(operacion == 3):
        val_pi()
        val_radio()
        area_circulo()
    elif(operacion == 4):
        break
    elif(operacion <= 5):
        print("Seleccione una opción válida")
    respuesta = input("Desea hacer otra operacion? si/no: ")
    if (respuesta == "no"):
        print("Hasta pronto")
        sys.exit(1)

print("Hasta pronto")
