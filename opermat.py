print("Suma de dos numero")

while True:
    try:
        n1 = int(input("numero 1: "))
        break
    except ValueError:
        print("El valor introducido no es un numero, introduce un numero")

while True:
    try:
        n2 = int(input("numero 2: "))
        break
    except ValueError:
        print("El valor introducido no es un numero, introduce un numero")
        
print ("La suma de los numero es: ", n1+n2)
        
        