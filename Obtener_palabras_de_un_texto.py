#Obtener palabras de un texto
texto = input("Escriba un texto: ")
n = len(texto)
texto_2 = ""
space = 0
for i in range(n):
    if (texto[i] != " ") & (i<n-1):
        texto_2 = texto_2 + "{}".format(texto[i])
    elif (texto[i] == " ") & (space == 0):
        print("La primera palabra es: " + texto_2)
        texto_2 = ""
        space += 1
    elif (texto[i] == " ")  & (space > 0):
        print("La palabra número {} es: {}".format(space+1,texto_2))
        texto_2 = ""
        space += 1
    elif (i == n-1) & (texto[i] != " "):
        texto_2 = texto_2 + "{}".format(texto[i])
        print("La última palabra es: " + texto_2)