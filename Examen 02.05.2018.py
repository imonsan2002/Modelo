cadena=input("Dame una cadena con mas de dos f ->")
primera=cadena .find("f")
segunda=cadena .rfind("f")
print(cadena[primera:segunda+1])