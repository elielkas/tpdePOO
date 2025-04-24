nombre1 = int(input("Entrer le nombre1 "))
operateur = input("Entrer le signe d'opération ")
nombre2 = int(input("Entrer le nombre2 "))

if operateur == "+":
    resultat = nombre1 + nombre2
    print(f"{nombre1}{operateur}{nombre2}={resultat}")
elif operateur == "-":
    resultat = nombre1 - nombre2
    print(f"{nombre1}{operateur}{nombre2}={resultat}")
elif operateur == "*" or operateur == "X":
    resultat = nombre1 * nombre2
    print(f"{nombre1}{operateur}{nombre2}={resultat}")
elif operateur == ":" or operateur == "/":
    if nombre2 == 0:
        print("ALERT : diviseur doit être different de 0")
    else:
        resultat = nombre1 / nombre2
        print(f"{nombre1}{operateur}{nombre2}={resultat}")