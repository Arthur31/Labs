#Récupération de la saisie utilisateur
heures, minutes, secondes = eval(input("Nombre d'heures : ")),eval(input("Nombre de minutes : ")),eval(input("Nombre de secondes : "))

#conversion
totalSecondes = (heures*3600) + (minutes * 60) + secondes

# Affichage
print('Nombre total de secondes : ', totalSecondes)


