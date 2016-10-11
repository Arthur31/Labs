#Récupération de la saisie utilisateur
x , y = eval(input('X : ')),eval(input('Y : '))

#Affichage avant permutation :
print('Avant permutation :', '\nX : ' , x, '\nY : ' , y )

# Permutation
vartmp = y
y = x
x = vartmp

#Affichage apres permutation :
print('Apres permutation :', '\nX : ' , x, '\nY : ' , y )
