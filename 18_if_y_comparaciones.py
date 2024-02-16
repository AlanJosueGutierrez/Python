#numero maximo que le damos
# != significa diferente
# == operador igual
# <= operador menor o igual
# >= operador mayor o igual

def max_num(l,m,n):
    if l <= n and m <= n:
        return n
    elif  n <= l and m <= l:
        return l
    elif  n <= m and l <= m:
        return m

n1 = input("Ingrese el número 1: ")
n2 = input("Ingrese el número 2: ")
n3 = input("Ingrese el número 3: ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

maximo = max(n1,n2,n3)

print("El numero más grande es: {}".format(maximo))


