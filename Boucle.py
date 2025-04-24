# boucle pour montrer le trucs
races_de_chien = ["golden retriever", "chihuahua", "terrien", "calin"]
for chien in races_de_chien:
    print(chien)
    
# Fonction range
for x in range(5):
    print(x)

for x in range(1, 11):
    print(f"{x} Bouteilles de bieres au levures!")

"Boucle while"
capaciteMax = 10
capacite_Actuele = 3
while capacite_Actuele < capaciteMax:
    print(f"la capacité actuelle est {capacite_Actuele}")
    capacite_Actuele += 1

#  break
for i in range(10):
    if i == 6: 
        break
    print(i)

# Continue 
liste = [1, 2, 3, 4, 5]
for element in liste:
    if element == 3:
        continue
    print(element)


