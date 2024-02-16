#Contar subcadenas que aparecen en un texto dado
#La función format nos permite incluir en una cadena, texto ordinario y caracteres de formateo
texto = input("Introduzca un texto: ")
subcadena = input("Introduzca una subcadena para saber el número de veces que aparece en el texto: ")
num_rep = texto.count(subcadena)

if num_rep ==1:
    print("La subcadena {} aparece una sola vez.".format(subcadena))
elif num_rep > 1:
    print("La subcadena {} aparece {} veces.".format(subcadena, num_rep))
else:
    print("La subcadena {} no aparece.".format(subcadena))