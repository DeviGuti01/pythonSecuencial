import math

cateto1 = float(input("Introduce el primer cateto: "))

cateto2 = float(input("Introduce el segundo cateto: "))

hipotenusa1 = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa del triangulo es:", hipotenusa1)