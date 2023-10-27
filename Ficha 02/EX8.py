
lang = input("Select the language:") 
match lang:
    case "PT":
        print("Bom dia!")
    case "EN":
        print("Good Morning!")
    case "FR":
        print("Bonjour!")
    case "GER":
        print("Guten Morgen!")
    case _:
        print("Idioma desconhecido :(")

