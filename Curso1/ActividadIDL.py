'''
Created on 19/07/2018

@author: David Barocio
'''

fruta = input("¿Comes frutas? (Teclea si o no)")
if fruta == "si":
    cantidad_fruta = int(input('¿Cuántas veces a la semana comes fruta? (escribe el número)'))

    if cantidad_fruta >= 5:
        print("¡Sigue así!")

        if cantidad_fruta >= 5:
            fruta_diaria = int(input('¿Cuántas frutas comes al día? (escribe el número)'))
            if fruta_diaria >= 2:
                print("Comes saludable")
            elif fruta_diaria < 2:
                print("Te recomendaría comer una fruta más")

    elif cantidad_fruta < 5 and cantidad_fruta > 2:
        print("Come más frutas a la semana")
    elif int (cantidad_fruta <= 2):
        print("Necesitas comer frutas")

else:
    fruta == "no"
    print("¡Necesitas comer frutas!")