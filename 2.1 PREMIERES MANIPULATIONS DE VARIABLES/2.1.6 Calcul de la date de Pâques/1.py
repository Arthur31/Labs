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

#Affichage du résultat
print("Différence de jours à partir du 31 mars pour l'an ",m, " : ", day - 31 )
