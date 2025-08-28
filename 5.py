

numero = int(input("Ingrese un número entero positivo: "))

if numero == 0:
    print("Representación binaria: 0")
else:
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    print("Representación binaria:", binario)
