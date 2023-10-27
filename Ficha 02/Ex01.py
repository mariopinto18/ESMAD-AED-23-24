# Lê um numero e determina se é par ou impar

numero = int(input("Número:"))
resto = numero % 2
if resto ==0:
    print("O número {0} é par" .format(numero))
else:
    print("O número {0} é ímpar" .format(numero))

