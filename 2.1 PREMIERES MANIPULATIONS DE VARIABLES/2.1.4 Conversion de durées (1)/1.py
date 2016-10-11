#Récupération de la saisie utilisateur
nbsecondes = eval(input('Nombre de secondes : '))

# Conversion
heures = nbsecondes // 3600
minutes = (nbsecondes - (heures * 3600)) // 60
secondes = nbsecondes - (heures * 3600) - (minutes * 60)

#Affichage
print('Heures : ',heures)
print('Minutes : ',minutes)
print('Secondes : ',secondes)


