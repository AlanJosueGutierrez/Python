#capitalize(): garantiza la primera letra en mayuscula
#lower(): convierte toda la cadena a minusculas
#upper(): convierte toda la cadena a mayuscualas
#title(): convierte la primera letra de cada palabra a mayusculas
#swapcase(): convierte mayusculas a minusculas y viceversa.
#count(): cuenta el numero de veces que aparece un texto dentro de otro texto
#len se usa para obtener el numero de caracteres de una cadena
#startswitch():devolverá True si el principio de la cadena coincide con la subcadena.
#endswitch(): devolverá True si el final de la cadena coincide con la subcadena
#find(): se usa para buscar la posición de una subcadena en una cadena en Python.
#format(): puede dar formato a los valores combinados para su visualización adecuada, como en el caso de números, fechas y horas.
#Uso de f para formatear cadenas de texto.

#Programa para saber si la primera letra esta en mayúscula y se pone el punto final
palabra = input("Escriba una palabra: ")
is_upper = palabra[0].isupper()
n1 = len(palabra)
point = palabra[n1-1] == "."

if (is_upper == True) & (point == True):
    print("Felicidades, sabes que la primera letra se escribe en mayúscula y al final se pone un punto. \n")
elif (is_upper == False) & (point == True):
    palabra_2 = palabra.capitalize()
    print("La primera letra se escribe en mayúscula, lo correcto sería escribir:\n" + palabra_2 )
elif (is_upper == True) & (point == False):
    print("Te faltó el punto al final, lo correcto sería escribir:\n" + palabra + ".")
elif (is_upper == False) & (point == False):
    palabra_2 = palabra.capitalize()
    print("Lo correcto sería escribir: \n" + palabra_2 + ".")

#Texto a mayusculas
while True:
    palabra = input("\nEscribe un texto completamente en mayusculas: ")
    if palabra.isupper():
        print("Este es el texto en minúsculas: \n" + palabra.lower())
        break

#Tittle
name1 = input("\nEscribe el nombre completo de una persona: ")
is_name = name1.istitle()

if is_name == True:
    print("El nombre fue escrito correctamente.")
else:
    name1 = name1.title()
    print("La primera letra de los nombres y apellidos se escribe en mayúsculas y las demás en minúsculas, lo correcto sería:\n" + name1)

#lstrip, rstrip, strip
texto = input("Escriba un texto:")

texto_l=texto.lstrip()
texto_r=texto.rstrip()
texto_s=texto.strip()
print("Este es el texto despues de aplicar \"lstrip\": " + texto_l + ".")
print("Este es el texto despues de aplicar \"rstrip\": " + texto_r + ".")
print("Este es el texto despues de aplicar \"strip\": " + texto_s + ".")

# Ejemplos trim en Python

texto = "    Esto es una prueba de espacios en blanco       "

print("Aplicando \"lstrip\" a texto: ---{}---".format(texto.lstrip()))
print("Aplicando \"rstrip\" a texto: ---{}---".format(texto.rstrip()))
print("Aplicando \"strip\" a texto: ---{}---".format(texto.strip()))




