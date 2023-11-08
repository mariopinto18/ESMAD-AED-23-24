
# Função que o nº de ocorrência de uma palavra, num texto
def countWord(text, txtFind):
    """
    It receives a string text, and a string word to find in the text
    It returns de number of occurences and positions
    """
    text = " " + text + " "
    txtFind = " " + txtFind + " "
    num = text.count(txtFind) 
    #---------------------------
    posInic=0           
    positions=""     # variável de saida com as diversas posições no texto
    for i in range(num):
        pos = text.find(txtFind, posInic) # pesquisa (find) no texto a partir da posição ant
        positions+= " " + str(pos+1)   
        posInic = pos + 1
    return num, positions     # devolve nº ocorrencias (num) e posições (positions)


text = input("Texto:")
txtFind = input("Pesquisa:")
num, positions = countWord(text, txtFind)
print("A palavra {0} ocorre {1} vezes no texto. Nas posições {2}" .format(txtFind, num, positions))




