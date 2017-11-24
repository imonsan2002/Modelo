columna = int(input("columna"))
fila = int(input("fila"))
columna2 = int(input("columna2"))
fila2 = int(input("fila2"))
numero1 = int(columna + fila)
numero2 = int(columna2 + fila2)
if (numero1 %2==0)and(numero2 %2==0):
  print("Iguales")
elif (numero1 %2!=0)and(numero2 %2!=0):
  print("Iguales")
else:
  print("Distinto")