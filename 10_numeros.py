#algunas funciones de math
#comb(n, k), Retorna el número de formas posibles de elegir k elementos de n, de forma ordenada y sin repetición. D 0 si k>n
from math import *
my_num=5
# ceil regresa el entrero proximo mayor a x, si x es entero regresa x
print(ceil(3.7))

#comb(n, k), Retorna el número de formas posibles de elegir k elementos de n, de forma ordenada y sin repetición. D 0 si k>n
print(comb(5, 4))

#copysign(x, y)
#Retorna un flotante con la magnitud (valor absoluto) de x pero el signo de y. En plataformas que admiten ceros con signo, copysign(1.0, -0.0) retorna -1.0.
print(copysign(2, -3))

#fabs(x)
#Retorna el valor absoluto de x.
print(fabs(-5.2))

#factorial(n)
#Retorna el factorial de n como un número entero. Lanza una excepción ValueError si n no es un entero o negativo.
print(factorial(3))

#floor(x)
#Retorna el «suelo» de x, el primer número entero menor o igual que x. Si x no es un flotante, delega en x.__floor__, que debería retornar un valor Integral.
print(floor(3.6))

#fmod(x, y)
#regresa el resto en numeros flotentes, para enteros es mejor usar x%y
print(fmod(820,820))

#floor(x)
#Retorna el «suelo» de x, el primer número entero menor o igual que x. Si x no es un flotante, delega en x.__floor__, que debería retornar un valor Integral.
print(floor(5.6))

#frexp(x)
#Retorna la mantisa y el exponente de x como el par (m, e). m es un flotante y e es un número entero tal que x == m * 2**e exactamente
print(frexp(5))

#sum(iterable)
#Retorna una suma precisa en coma flotante de los valores de un iterable.
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

#gcd(*integers)
#Retorna el máximo común divisor de los argumentos enteros.
print(gcd(30,36))

#isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
#Retorna True si los valores a y b están cerca el uno del otro y False en caso contrario.
print(isclose(3, 9, abs_tol=5.9))

#isfinite(x)¶
#Retorna True si x no es infinito ni NaN, o False en caso contrario. (Ten en cuenta que 0.0 es considerado finito.)
print(isfinite(8.3))

#https://docs.python.org/es/3/library/math.html

