cantidad = 0
suma = 0
while True:
  cantidad += 1
  n = int(input('Dime un número:'))
  suma = suma + n
  if n == 0:
    break
media=suma//cantidad
print('El número de números introducidos es' +' '+ str(cantidad-1))
print('La suma de los números introducidos son'+' '+str(suma))
print("La media de los numeros introducidos es"+" "+str(media))