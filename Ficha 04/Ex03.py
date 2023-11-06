
# Função que recebe um numero e determina se é um numero abundante (True) ou não (False)
def abundante(numero:int):
    """
    recebe um numero inteiro e devolve se é um numero abundante (True) ou não (False)
    """
    somaDivisores=0
    for i in range (1, numero):  # pecorrer intervaloer de 1 até ao númeor
        if numero % i ==0:
            somaDivisores+= i
    if somaDivisores>numero:
        return True
    else:
        return False


numero= int(input("Indique um número:"))
if abundante(numero)== True:
    print("o numero {0} é abundante" .format(numero))
else:
     print("o numero {0} NÃO é abundante" .format(numero))
