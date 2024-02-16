print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")
print("Giraffe \Academy")
phrase = "Giraffe Academy"
phrase_2 = "Cool"

print("\nphrase es igual a: " + phrase)
print("\nphrase_2 es igual a: " + phrase_2)

print("\n" + phrase + " is "+ phrase_2)

print("\nA continuacion se mostrará phrase en mayúsculas")
print("Giraffe Academy".upper())

print("\nA continuacion se mostrará phrase en minúsculas")
print(phrase.lower())

#convierte phrase a mayusculas y devuelve True si son mayusculas
print("\nRegresará True si convirtió a mayúsculas la cadena")
print(phrase.upper().isupper())

#longitud de una cadena
print("La longitud de {} es: {}".format(phrase_2, len(phrase_2)))
#print(len(phrase_2))

#para obtener caracteres individuales de una cadena es con []
#python inicia en 0 y si quiero obtener toda la cadena necesito poner la longitud de la cadena
print(phrase_2[0:len(phrase_2)])
print(phrase_2[len(phrase_2)-1])
#index devuelve el numero en el que esta el primer subconjunto de cadena
print(phrase.index("ad"))

#replace
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

print(5==2)