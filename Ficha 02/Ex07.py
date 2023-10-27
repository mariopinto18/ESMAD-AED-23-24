# Exercicio 7
print("\t\t\t\t\tPlanets")
print("\t\t\t\t1 - Mercury")
print("\t\t\t\t2 - Venus")
print("\t\t\t\t3 - Mars")
print("\t\t\t\t4 - Jupiter")
print("\t\t\t\t5 - Saturn")
print("\t\t\t\t6 - Uranus")

peso = float(input("\n\n\tYour weight (kg):"))
planeta = int(input("\n\n\tPlanet code:"))

if planeta == 1:
    gravidade = 0.37
elif planeta == 2:
    gravidade = 0.88
elif planeta == 3:
    gravidade = 0.38
elif planeta == 4:
    gravidade = 2.64
elif planeta == 5:
    gravidade = 1.15
elif planeta == 6:
    gravidade = 1.17
else:
    print("invalid planet code!:( ")


match planeta:
    case 1: gravidade = 0.37
    case 2: gravidade = 0.88
    case 3: gravidade = 0.38
    case 4: gravidade = 2.64
    case 5: gravidade = 1.15
    case 6: gravidade = 1.17
    case _: 
        print("Planet code invalid! :(")
        exit()
            
pesoPlaneta = peso*gravidade
print("\n\tYour weight {:.2f} kg, \n\ton the planet {:.0f} \n\twould be {:.2f}" .format(peso, planeta, pesoPlaneta))
