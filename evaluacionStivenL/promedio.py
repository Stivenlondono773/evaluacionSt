numeros = []

for i in range(10):
  numero = int(input("Ingrese un número: "))
  numeros.append(numero)

print("Los números que ingresaste son:", numeros)

promedio = sum(numeros) / len(numeros)

print("El promedio de la lista es:", promedio)

