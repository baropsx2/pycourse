
'''
Created on 19/07/2018

@author: David Barocio
'''
def valores():
   global num1, num2
   num1 = int(input("Introduzca el primer número: "))
   num2 = int(input("Introduzca el segundo número: "))
def suma():
   print("El resultado de la suma de", num1, "más", num2, "es: ", num1 + num2)
def resta():
   print("El resultado de la resta de", num1, "menos", num2, "es: ", num1 - num2)
def multiplicacion():
   print("El resultado de la multiplicación de", num1, "por", num2, "es: ", num1 * num2)
def division():
   if (num2 == 0):
       print("No se puede dividir entre 0")
   else:
       print("El resultado de la división de", num1, "por", num2, "es: ", num1 / num2)
def modulo():
   if num1 % 2 == 0:
       print("El primer número introducido es múltiplo de 2")

print("Calculadora de operaciones básicas")
print("Seleccione la operación a calcular")
while(True):
   print("1 - Suma")
   print("2 - Resta")
   print("3 - Multiplicación")
   print("4 - División")
   operacion = int(input("Escriba el número de opción para realizar la operación"))
   if (operacion == 1):
       valores()
       suma()
       modulo()
   elif (operacion == 2):
       valores()
       resta()
       modulo()
   elif (operacion == 3):
       valores()
       multiplicacion()
       modulo()
   elif (operacion == 4):
       valores()
       division()
       modulo()
   break

