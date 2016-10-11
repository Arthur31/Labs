# Récupération du prix Hors Taxes
prixHt = eval(input('Prix HT du produit : '))

# Récupération de la Tva
Tva = eval(input('Tva : '))

# Récupération du nombre de produits
nbProduits = eval(input('Nombre de produits : '))

# Calcul du résultat
resultat = prixHt * (1+Tva) * nbProduits

# Affichage du résultat
print('Total TTC : ', resultat)