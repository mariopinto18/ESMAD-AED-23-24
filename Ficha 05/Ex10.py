def printCharLine(text, number):
    """
    receives a text and prints @number characters by line
    """
    while (len(text)>number):   # enquanto o comprimento do texto > numero de caracteres a imprimir
        print(text[0:number])
        text=text[number:]
    print(text)



text = input("Texto:")
while True:
    try:
        number = int(input("\nNº caracteres a imprimir por linha:"))
        if number <5 or number >12:
            raise ValueError()
    except ValueError:
        print(" O numero inserido não é valido. Deve inserir um número entre 5 e 12 caracteres por linha!")
    except:
        print("upss... ocorreu um erro!")
    else:
        break

printCharLine(text, number)

