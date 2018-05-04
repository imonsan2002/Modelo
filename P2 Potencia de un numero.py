def potencia(x,n):
  if n==0:
    return 1
  return x * potencia(x,(n-1))

h=int(input("Dame un numero"))
l=int(input("Dame un numero para elevar el anterior"))
print(potencia(h,l))