# Récupération des infos via une affectation multiple
prixHt , Tva, nbProduits = eval(input('Prix HT du produit : ')),1 + eval(input('Tva : ')),eval(input('Nombre de produits : '))

# Calcul du résultat
resultat = prixHt * Tva * nbProduits

# Affichage du résultat
print('Total TTC : ', resultat)



