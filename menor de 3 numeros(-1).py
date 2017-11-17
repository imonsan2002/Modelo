x = int(input("¿numero 1?"))
y = int(input("¿numero 2?"))
z = int(input("¿numero 3?"))
if x <= y:
   MENORprimeros = x
if y <= x:
  MENORprimeros = y
if MENORprimeros <= z:
  print(MENORprimeros)
if z <= MENORprimeros:
  print(z)