# Simulador de IMC

peso   = float(input("Indique o seu peso(Kg) : "))
altura = float(input("Indique a sua altura(m): "))

imc= peso / altura**2
print("\n\t\tIMC= {:.2f}" .format(imc))


if imc < 18.5:
    print("\tUnder weight")
elif imc <= 24.9:
    print("\tHealthy")
elif imc <= 29.9:
    print("\tOverweight")
elif imc <= 34.9:
    print("\tObesity Grade I")
elif imc <= 39.9:
    print("\tObesity Grade II (severe)")
else:
    print("\tObesity Grade III (morbid)")


input()