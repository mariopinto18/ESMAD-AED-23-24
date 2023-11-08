# Função que recebe um texto e verifica se é capicua ou não
def capicua(texto):
    """
    Receives a string and returns a boolean value if it is, or not, capicua
    """
    invTexto = "" 
    for i in range (len(texto)-1, -1, -1):
        invTexto+= texto[i]
    if texto == invTexto:
        return True
    else:
        return False


texto = input("Insira um texto:")
if capicua(texto.lower()) == True:
    print("a palavra {0} é capicua" .format(texto))
else:
    print("a palavra {0} não é capicua" .format(texto))


