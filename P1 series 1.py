n1 = int(input("numero 1? ="))
n2 = int(input("numero 2? ="))
if n1 > n2:
  for z in range(n2,n1 + 1):
    print(z)
elif n2 > n1:
  for y in range(n1,n2 + 1):
    print(y)
