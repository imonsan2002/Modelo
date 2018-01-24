n = int(input("numero? = "))
i = 0
for numero in range(n+1):
  i = i + numero**3
print(i, "cubo de los numeros es ", numero)