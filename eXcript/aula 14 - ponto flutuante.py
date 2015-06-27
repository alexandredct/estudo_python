num_int = 3
num_dec = 8.5
val_str = "Isso é um texto"
print(num_int)

print("o valor é:",num_int)
print("o valor é:%i" %num_int)
print("o valor é: %i" + str(num_int))

print("Concatenando decimal:",num_dec)#irá imprimir 8.5
print("Concatenando decimal: %f" %num_dec) #irá imprimir 8.500000
print("Concatenando decimal: %.2f" %num_dec) #irá imprimir 8.50
print("Concatenando decimal: " + str(num_dec)) #instâncias de tipos diferentes devem ser convertidos a um tipo comum sempre!

print("Concatenando strings:",val_str)
print("Concatenando strings: %s" %val_str)
print("Concatenando strings: " + val_str)