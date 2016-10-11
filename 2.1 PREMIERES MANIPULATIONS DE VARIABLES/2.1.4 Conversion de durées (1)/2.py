#Récupération de la saisie utilisateur
nbsecondes = eval(input('Nombre de secondes : '))

# Conversion
heures, nbsecondes  = nbsecondes // 3600, nbsecondes % 3600
minutes,nbsecondes = nbsecondes // 60, nbsecondes % 60

#Affichage
print('Heures : ',heures)
print('Minutes : ',minutes)
print('Secondes : ',nbsecondes)

