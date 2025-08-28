x = float(input("Ingrese el valor de x: "))

if x < 0:
    f = x**2
elif x <= 10:
    f = 2*x + 1
else:
    f = 3*x - 5

print("f(x) =", f)
