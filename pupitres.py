c1 = int(input("clase 1:"))
c2 = int(input("clase 2:"))
c3 = int(input("clase 3:"))
pupitres1 = c1 // 2 + c1%2
pupitres2 = c2 // 2 + c2%2
pupitres3 = c3 // 2 + c3%2
pupitres=pupitres1+pupitres2+pupitres3
print("necesito "+str(pupitres)+" pupitres")
