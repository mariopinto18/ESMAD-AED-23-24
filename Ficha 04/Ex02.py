
def somatorio(lim1: int, lim2: int):
    """
    Recebe 2 números inteiros e determina o somatório de todos os inteiros no intervalo indicado 
    """
    if lim1 > lim2:     # no caso de lim1 ser superior a lim2
        temp = lim1     # trocamos o conteúdo das variáveis
        lim1 = lim2     # de forma a que lim1 seja sempre < lim2
        lim2 = temp
    soma=0
    for i in range(lim1, lim2+1):
        soma+=i
    print("soma de numeros é {0}" .format(soma))


lim1 = int(input("Insira o primeiro numero: "))
lim2 = int(input("Insira o segundo  numero: "))

somatorio(lim1, lim2)      # imprimie somatorio de numeros inteiros entre [1-3]
somatorio(3,6)      # imprimie somatorio de numeros inteiros entre [3-6]
