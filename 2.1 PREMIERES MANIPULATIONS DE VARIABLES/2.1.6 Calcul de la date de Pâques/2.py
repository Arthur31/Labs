# Récup de l'année
m = eval(input("Entrer l'année :"))

# Calcul du jour :
n = m - 1900
a = n % 19
b = ((7 * a) + 1) // 19
c = ((11 * a) - b + 4) % 29
d = n // 4
e = (n - c + d + 31 ) % 7
day = 31 +(25-c-e)

# Affichage correct du mois (chap : 02 - Structures conditionnelles et itératives)
month = " avril" if day - 31 > 0 else " mars"

# Affichage de la date :
print("Paques pour l'année ",m," est le :",day%31,month)
