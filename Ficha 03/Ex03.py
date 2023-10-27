# determina o fatorial de um número

numero = int(input("Indique um número: "))

while numero <0:
    print("Indiqe, p.f., um número inteiro >=0")
    numero = int(input("Indique um número: "))
# Temos a certeza de ter um numero >=0

fatorial=1                       # inicializa fatorial a 1
for i in range(1, numero+1):     # repete do numero lido até 1 (decrescente)
    fatorial*=i

print("Fatorial de {0} é {1}" .format(numero, fatorial))

