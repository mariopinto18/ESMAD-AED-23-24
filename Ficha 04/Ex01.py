def fibonacci(ntermos:int):
    """
    devolve os primeiros ntermos da sequência de Fibanocci
    """
    if ntermos >= 1:        # trata 1º termo da sequencia
            result = "0"
    if ntermos >= 2:        # trata 2º termo da sequencia
            result = result + ", 1"
    penultimo = 0
    ultimo = 1
  # calcula todos os termos a partir do terceiro
    for i in range(3, ntermos+1):   # para todos a partir do 3º termo
        novo = penultimo+ultimo     # cada termo resulta da soma dos 2 anteriores
        result = result + ", " + str(novo)
        penultimo = ultimo
        ultimo = novo
    print("\n\n\n\t\t\t Primeiro %s termos da sequência de Fibonacci: %s"  %(ntermos, result))

# Exemplos da chamada da função fibonacci
numero = int(input('Indique nº de  termos a imprimir:'))
fibonacci(numero) # Imprime numero termos
fibonacci(5)      # Imprime 5 termos
fibonacci(10)     # Imprime 10 termos


