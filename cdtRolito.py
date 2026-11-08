cantidadDinero = float(input("Ingrese la cantidad de dinero que desea depositar en Cdt de Rolito: "))

porcentajeInteres = float(input("Este es tu porcentaje de rendimiento en Cdt de Rolito: "))

periodo = float(input("El periodo de tiempo de tu dinero en Cdt de Rolito fue: "))

valorInteres = (cantidadDinero * porcentajeInteres * periodo) / 360

impuesto = valorInteres * 0.07

total = cantidadDinero + valorInteres - impuesto

print("El valor total es:", total)
print("El impuesto es:", impuesto)
print("El valor de intereses es:", valorInteres)