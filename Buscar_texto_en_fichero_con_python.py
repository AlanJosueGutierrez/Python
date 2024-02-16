import os.path

#Para este ejemplo vamos a pedir al usuario que introduzca
#la ruta y el nombre de un fichero de texto
#Y pedirá también que introduzca una letra, palabra o frase
#El programa mostrará si existe ese texto en el fichero

ruta = input("Introduzca la ruta con el nombre del archivo txt: ")

#Comprobamos si existe el fichero
if os.path.isfile(ruta):
    texto = input("Introduzca el texto a buscar en el fichero: ")
    #Leemos el fichero y lo almacenamos en una variable
    fichero = open(ruta)
    contenido = fichero.read()
    #Buscamos el texto en el fichero
    posicion = contenido.find(texto)
    if posicion >= 0:
        print("Se ha encontrado el texto en el fichero, en la posición ", posicion)
        exit(3) #Cerramos aplicación con código de salida 3
    else:
        print("No se ha encontrado el texto en el fichero")
        exit(2) #Cerramos aplicación con código de salida 2
    #Cerramos el fichero
    fichero.close()
else:
    #En caso de no existir salimos del programa con código de salida 1
    print("No se ha encontrado el archivo en la ruta")
    exit(1)
