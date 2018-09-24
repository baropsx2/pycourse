#numeroInt = input("Ingresa un Numero: ")
#numeroStr = int(numeroInt)

#if(numeroInt > 2):
#     print(numeroStr + "1")
#elif(numeroInt == 2):
#     print(numeroStr + "2")
#else:
#     print(numeroStr + "3")

# -*- coding: utf-8-*-
respuesta = "si"
while respuesta != "no":
    print
    ''' 
CALCULADORA BASICA ----->
1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR
5) SALIR'''
    opcion = input("Ingrese el numero de su opcion: ")
    if opcion > 0 and opcion < 6:
        primer_numero = input("Ingrese un Numero: ")
        segundo_numero = input("Ingrese otro Numero: ")
        if opcion == 1:
            suma = primer_numero + segundo_numero
            print("SUMA: ", suma)
        elif opcion == 2:
            resta = primer_numero - segundo_numero
            print("RESTA: ", resta)
        elif opcion == 3:
            multiplicacion = primer_numero * segundo_numero
            print("MULTIPLICACIÓN: ", multiplicacion)
        elif opcion == 4:
            if segundo_numero == 0:
                print("ERROR")
            else:
                division = primer_numero / segundo_numero
                print("DIVISIÓN", division)
        elif opcion == 5:
            print("HASTA LUEGO!")
            sys.exit()
    respuesta = raw_input("Desea hacer otra operacion? [Si/No]: ")
