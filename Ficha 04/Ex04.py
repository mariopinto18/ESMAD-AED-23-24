# Função que recebe n argumentos de entrada, e calcula a sua média
def media(*numeros):    # nº indeterminado de argumentos de entrada
    """
    Recebe um conjunto de numeros inteiros e devolve a sua média
    """
    soma=0
    for i in range(len(numeros)):   # percorre todos os argumentos de entrada
        soma+= numeros[i]           # soma os valores passados pelo argumento numeros
    return soma/len(numeros)        # devolve a média



valorMedio = media(10,20,30, 99)
print("{:.2f}" .format(valorMedio))

print("{:.2f}" .format(media(15, 30)))
print("{:.2f}" .format(media(5,10, 15, 20)))

