def array_invertido(array_normal):
    return list(reversed(array_normal))

array_string = []

num = int(input("Introduzca la cantidad de elementos del array: "))

for i in range(num):

    valor = str(input("Introduzca un elemento: "))
    array_string.append(valor)

print(f"el array normal es: {array_string}")
print(f"el array invertido es: {array_invertido(array_string)}")

