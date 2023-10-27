""" 
Simulador de esforço cardíaco
Nas mulheres FCM = 226 - idade.
Nos homens FCM=  220 - idade
 """

gender = input("\n\n\n\tGender(M/F): ")
if gender.lower() != "m" and gender.lower() != "f":
    print("Invalid Gender")
    exit()
age = int(input("\n\n\tAge: "))
if gender.upper() == "F":
    mhr = 226-age
else:
    mhr = 220-age
print("\n\t\t\tMHR= {0} bpm" .format(mhr))

