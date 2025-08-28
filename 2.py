# Programa: Contar dígitos primos en un número entero positivo

numero = int(input("Ingrese un número entero positivo: "))
contador = 0

while numero > 0:
    digito = numero % 10  # último dígito
    if digito in [2, 3, 5, 7]:
        contador += 1
    numero = numero // 10  # eliminar el último dígito

print("Cantidad de dígitos primos:", contador)
