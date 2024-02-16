import sys
# Lee x de l a t e rminal
x = int(input("Ingrese un numero natural: " ) )
#Implementacion de una v e r i f i c a c i o n no opt ima de l a c onj e tur a de Co l l a t z
while x != 1:
    if x%2 == 0:
        x = x/2
    else:
        x = x*3 + 1
    sys.stdout.write(str(int(x)) + ", ")
print("La cadena regresa al 1." )