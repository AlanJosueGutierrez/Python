#n1 = float(input("Ingrese el primer numero: "))

#while True:
#    op = input("Ingrese el operador (+, -, *, /): ")
#    if op == "+" or op == "-" or op == "*" or op == "/":
#        break

#n2 = float(input("Ingrese el segundo número: "))

def operacion(op1,n,m):
    if op1 == "+":
        return n+m
    elif op1 == "-":
        return n-m
    elif op1 == "*":
        return  n*m
    elif op1 == "/":
        return n/m
    else:
        return "Operador inválido"

#resp = operacion(op,n1,n2)
#print("El resultado de hacer {}{}{} es: {}".format(n1,op,n2,resp))

cuenta = input("Ingrese los numeros y la operación que desea realizar: ")
k = len(cuenta)
n_1 = ""
simbolo = ""
num_simbolos = 0
m_1 = 0.0
r = 0.0
for i in range(k):
    #print(i)
    if ((cuenta[i] != "+") == (cuenta[i] != "-") == (cuenta[i] != "*") == (cuenta[i] != "/")) and (num_simbolos == 0):
        n_1 = n_1 + cuenta[i]
        #print(n_1)
    elif ((cuenta[i] == "+") or (cuenta[i] == "-") or (cuenta[i] == "*") or (cuenta[i] == "/")) and (num_simbolos == 0):
        simbolo = cuenta[i]
        m_1 = float(n_1)
        n_1 = ""
        num_simbolos += 1
        #print(simbolo + "{}".format(m_1))
    elif ((cuenta[i] != "+") == (cuenta[i] != "-") == (cuenta[i] != "*") == (cuenta[i] != "/")) and (num_simbolos > 0) and (i < k-1):
        n_1 = n_1 + cuenta[i]
        #print(n_1)
    elif ((cuenta[i] == "+") or (cuenta[i] == "-") or (cuenta[i] == "*") or (cuenta[i] == "/")) and (num_simbolos > 0):
        m_2 = float(n_1)
        r = operacion(simbolo, m_1, m_2)
        m_1 = r
        n_1 = ""
        simbolo = cuenta[i]
        #print("m_2={}, r={} ".format(m_2,r))
    elif i == k-1:
        n_1 = n_1 + cuenta[i]
        m_2 = float(n_1)
        r = operacion(simbolo, m_1, m_2)

print("El resultado es {}".format(r))







