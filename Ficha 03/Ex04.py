# Jogo Adivinha o número
# Dado um numero aleatorio, o utilizador deve adivinhá-lo
import random

resposta = "S"
while resposta.upper() == "S":
# Inicio do jogo-------
    numero = random.randint(1,50)  # gera numero aleatorio entre 0 e 50
    palpite = int(input("Indique o seu palpite: "))
    tentativas = 1
    while numero != palpite and tentativas <10:     # controla o funcionamento de 1 jogo
        if palpite > numero:
                print("O número a adivinhar é MENOR \n")
        elif palpite < numero:
                print("O número a adivinhar é MAIOR \n")
        palpite = int(input("Indique o seu palpite: "))
        tentativas+= 1

    if numero == palpite:
        print("Parabéns! Acertou em {0} tentativas" .format(tentativas))
    else:
        print("Esgotou as 10 tentativas! :( ")

    resposta = input("Novo Jogo(S/N)?:")    # Pergunta se deseja reiniciar
                
print("Obrigado, Volte sempre!!")     # mensagem final, quando o utilizador 
                                      # pretende sair