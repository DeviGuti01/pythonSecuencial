salarioBase = float(input("Ingrese el salario base del empleado: "))

aporteSalud = salarioBase * 0.04
aportePension = salarioBase * 0.04

descuento = aporteSalud + aportePension
salarioNeto = salarioBase - descuento

print("El aporte a salud es: $", aporteSalud)
print("El aporte a pension es: $", aportePension)
print("El descuento total es: $", descuento)
print("El salario neto a pagar es: $", salarioNeto)