print(6%2)#retorna o resto, 0 no caso

print(10%3)#retorna o resto, 1 no caso

#Número dívisível
print(900%100==0)#retornará true

num1 = float(input("Digite um número: "))#deve ser convertido para realizar operações
num2 = float(input("Digite um segundo número: "))

divisao = num1 / num2
resto = num1 % num2

print(num1, "dividido por",num2,"é igual",divisao,"com resto",resto)
