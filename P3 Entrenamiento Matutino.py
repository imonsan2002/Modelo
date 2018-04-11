km1=(int(input("Cuantos kilometros puedes correr? ->")))
km2=(int(input("Cuantos kilometros tienes que correr? ->")))
dias = 0
while km1<km2:
  i = int(km1) * 0.1
  km1 = km1+i
  dias=dias+1
print(dias)