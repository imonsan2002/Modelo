a = int(input("numero 1"))
b = int(input("numero 2"))
c = int(input("numero 3"))
if (a == b == c):
  print("iguales")
if (a != b== c):
  print("2 numeros iguales")
elif (b != c == a):
  print("2 numeros iguales")
elif (c != b == a):
  print("2 numeros iguales")
if (a != b != c) and (a != c != b):
  print("distintos")