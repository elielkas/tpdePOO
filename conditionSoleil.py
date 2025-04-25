avecSoleil = True 
en_semaine = False
if avecSoleil and not en_semaine: 
    print("On va à la plage")
elif avecSoleil and en_semaine: 
    print("On va au travail")
else: 
    print("On reste à la casa")