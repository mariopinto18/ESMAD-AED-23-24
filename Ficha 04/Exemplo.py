
def fatorial(num):
    """
    Receives a int number and return the fatorial of a number passed by argument
    """
    fatorial =1
    for i in range (num, 1, -1):
        fatorial*=i
    print("fatorial de {0} é {1}" .format(number,fatorial))



number = int(input("Indicate a number:"))
fatorial(number)

