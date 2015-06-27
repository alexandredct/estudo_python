a = 1
b = 2
c = 7

def soma_num(a,b):
    c = a+b
    return c

def imprime(a):
    for b in range(a):
        print(b)

print(soma_num(a,b))
print("c = " + str(c))
imprime(5)
print(soma_num(7,3))
imprime(3)
