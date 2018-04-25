cantidad = 0
big = 0
while True:
  cantidad += 1
  n = int(input('Dime un número:'))
  if n < big:
    big = big
  else:
    big = n
  if n == 0:
    break
print('El número de números introducidos es' +' '+ str(cantidad-1))
print('El número mayor es' +' '+ str(big))