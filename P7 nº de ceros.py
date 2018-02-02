n = int(input("cantidad numeros? ="))
j=0
for i in range(1, n+1):
  x = int(input("dime el " + str(i) + "ºnumero"))
  if (x==0):
    j=j+1
    print("+un 0")
  else:
    print("no es 0")
print(j)

    
  