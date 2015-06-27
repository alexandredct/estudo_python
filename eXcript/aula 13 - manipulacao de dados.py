num_int = 3
num_dec = 8.5
val_str = "Isso é um texto"
print(num_int)

#Forma 1 de impressão de tipos diferentes
print("o valor é:",num_int)#irá adicionar espaço automaticamente!

#Forma 2 de impressão de tipos diferentes
print("o valor é:%i" %num_int)#usando marcador; não irá adicionar espaço;

#Forma 3 de impressão de tipos diferentes
print("o valor é: %i" + str(num_int)) #conversão para string