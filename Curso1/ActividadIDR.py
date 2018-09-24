'''
Created on 26/07/2018

@author: David Barocio
'''
hora_1 = 0
min1 = 0
min2 = 0
seg1 = 0
seg2 = 0

while min1 <= 5:
    while min2 <= 9:
        while seg1 <= 5:
            while seg2 <= 9:
                print("El tiempo es " + str(hora_1) + ":" + str(min1) + str(min2) + ":" + str(seg1) + str(
                    seg2))
                seg2 += 1
            seg2 = 0
            seg1 += 1
        seg2 = 0
        seg1 = 0
        min2 += 1
    min2 = 0
    min1 += 1
hora2 = 0
hora_1 += 1

print ("El tiempo es " + "1:00:00")

