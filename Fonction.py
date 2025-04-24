# utiliser une fonction avec qui retourne quelque chose 
def calculerSomme(a, b):
    resultat = a+b
    return resultat


somme = calculerSomme(2, 3)
print(somme)

# Notion sur les fonction
'''def afficher_message():
    print("Bonjour Rine comment tu vas??")

afficher_message()'''


def afficherNomPrenom(nom, prenom):
    print("Nom : ", nom)
    print("Prenom : ", prenom)
    

NomPrenom = afficherNomPrenom("Eliel", "Kasonia")
print(NomPrenom)