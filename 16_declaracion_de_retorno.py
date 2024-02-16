#podemos usar return en las funciones para
#recuperar información de la función.
#si se pone codigo despues del return el código no funcionará
def cube(num):
    return num*num*num

num1 = input("Ingrese un numero: ")
f=float(num1)
cubo = cube(f)
print(cubo)