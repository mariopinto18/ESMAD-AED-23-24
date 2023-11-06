def primo(number):
    """
    It return a boolean value, True if de number os prime, False is the number is not prime
    """
    primo = True
    for i in range(2, number):  # o divisor varia entre 2 e o numero-1
        resto = number % i
        if resto == 0:          # quando encontro um resto 0 => não é primo
            primo = False
            break
    return primo


number = int(input("Indicate a number:"))
estado = primo(number)
if estado==True:
    print("O numero {0} é primo" .format(number))
else:
  print("O numero {0} não é primo" .format(number))

