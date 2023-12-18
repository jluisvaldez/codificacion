# -*- coding: utf-8 -*-
print("Suma de dos numeros con controles")
# Controlar el error de conversion

while True:
    try:
        n1 = int(input("primer numero: "))
        break
    except ValueError:
        print("El valor introducido no es un numero. Intenta de nuevo")

while True:
    try:
        n2 = int(input("Segundo numero: "))
        break
    except ValueError:
        print("El valor introducido no es un numero. Intenta de nuevo")

print ("La suma de los dos numeros es: ", n1+n2)