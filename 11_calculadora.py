print("Esta es una calculadora básica:\n ")

while True:
    operation = input("Ingrese 1 para sumar, 2 para multiplicar y 3 para dividir: ")
    if operation == "1":
        num_1 = input("Número 1: ")
        num_2 = input("Número 2: ")
        sum = float(num_1) + float(num_2)
        print("la suma de los numeros es {}".format(sum))
        break
    elif operation == "2":
        num_1 = input("Número 1: ")
        num_2 = input("Número 2: ")
        mult = float(num_1) * float(num_2)
        print("la multiplicación de los números es {}".format(mult))
        break
    elif operation == "3":
        num_1 = input("Número 1: ")
        num_2 = input("Número 2: ")
        div = float(num_1) / float(num_2)
        print("la división de los números es {}".format(div))
        break


