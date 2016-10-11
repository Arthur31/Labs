
# Informer que l'on veut récupérer le prix Hors Taxes
print('Prix HT du produit ',end=': ')
# Récupération de l'entrée de l'utilisateur ( variable de type str )
prixHt = input()

# Informer que l'on veut récupérer la Tva
print('Tva ',end=': ')
# Récupération de l'entrée de l'utilisateur ( variable de type str )
Tva = input()

# Informer que l'on veut récupérer le Nombre de produits
print('Nombre de produits ',end=': ')
# Récupération de l'entrée de l'utilisateur ( variable de type str )
nbProduits = input()

# Calcul du résultat avec conversion des type str en float
resultat = float(prixHt) * (1+float(Tva)) * float(nbProduits)

#Affichage du résultat
print('Total TTC : ', resultat)



