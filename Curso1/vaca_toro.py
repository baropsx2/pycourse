'''

Created on 04/09/2018

@author: David Barocio
'''
'''
Bienvenido al Juego de Vacas y Toros!
  Teclea un numero de 4 dígitos:
  >>> 1234
  2 Vacas, 2 Toros
  >>> 1256
  3 Vacas, 1 Toros
  ...
'''

import random

#Funciones del juego
def preguntarUsuario():
    return input("Escribe un número de 4 dígitos o escribe exit para salir: ")

def valida_numeros(n_usuario, n_random):
    vacas = 0
    toros = 0
    for x in range(0,len(n_random)):
        if n_usuario[x] == n_random[x]:
            vacas += 1
        elif n_usuario[x] in n_random:
            toros += 1
    print('{}: {} vacas, {} toros'.format(n_usuario,vacas,toros))

contador = 0

if __name__=="__main__":
    numero_random = random.randint(1000,9999)
    while(True):
        num_usuario = preguntarUsuario()
        if num_usuario == 'exit':
            print('Número total de intentos:', contador)
            break
        elif int(num_usuario) == numero_random:
            print('Felicitaciones! \nAdivinaste el número correcto!\n{} 4 vacas, 0 toros\nJuego Terminado'.format(numero_random))
            break
        else:
            valida_numeros(num_usuario,str(numero_random))
            contador += 1
            print('Número total de intentos:', contador)