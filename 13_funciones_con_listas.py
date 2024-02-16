#algunas funciones comunes en listas son:
#print() muestra toda la lista
#
#
lucky_numbers = [4, 8, 15, 16, 23, 42, 0, -5, 5]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#print() muestra toda la lista
print(friends)

#extend() extiende la lista
friends.extend(lucky_numbers)
print(friends)

#append() agrega un elemento al final
friends.append("Creed")
print(friends)

#insert() para insertar un elemento en una posición específica
friends.insert(1, "Kelly")
print(friends)

#remove() elimina elementos, si el elemento no está erroja un error
friends.remove("Jim")
print(friends)

#clear() para eliminar todos lo elementos de una lista
friends.clear()
print(friends)
z=len(friends)
print(z)

#pop() elimina el último elemento de una lista
friends = ["Kevin", "Karen", "Jim","Jim", "Oscar","Jim", "Toby"]
friends.pop()
print(friends)


#index() para obtener el indice de un elemento de la lista
print(friends.index("Oscar"))#recordemos que las cadenas comienzan con 0

#count() cuenta el número de veces que esta ese elemento
print(friends.count("Jim"))

#sort() ordena la lista
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

#reverse() ordena la lista desde el último elemento al primero
lucky_numbers = [4, 8, 15, 16, 23, 42, 0, -5, 5]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.reverse()
print(friends)

#copy() se usa para coíar elementos de una lista
friends_2 = friends.copy()
print(friends_2)

