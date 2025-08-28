nums = [float(input("Ingrese un número racional: ")) for _ in range(3)]

positivos = sum(1 for n in nums if n > 0)
negativos = sum(1 for n in nums if n < 0)
ceros = sum(1 for n in nums if n == 0)

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
