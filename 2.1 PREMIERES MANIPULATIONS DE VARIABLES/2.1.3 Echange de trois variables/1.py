#Récupération de la saisie utilisateur
x , y, z = eval(input('X : ')),eval(input('Y : ')),eval(input('Z : '))

#Affichage avant permutation :
print('Avant permutation :', '\nX : ' , x, '\nY : ' , y, '\nZ : ' , z )

# Permutation
x , y, z = y, z, x

#Affichage apres permutation :
print('Apres permutation :', '\nX : ' , x, '\nY : ' , y, '\nZ : ' , z )
