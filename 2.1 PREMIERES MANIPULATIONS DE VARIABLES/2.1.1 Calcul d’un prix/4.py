# Sans utiliser de variables sur ligne unique
print('Total TTC : ', eval(input('Prix HT du produit : ')) * (1 + eval(input('Tva : '))) * eval(input('Nombre de produits : ')))

# Meme chose sur plusieurs lignes ( plus clair visuellement ? )
print('Total TTC : ',
      eval(input('Prix HT du produit : ')) *
      (1 + eval(input('Tva : '))) *
      eval(input('Nombre de produits : '))
      )
