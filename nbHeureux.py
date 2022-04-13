# Ce programme dit si un nombre est heureux ou pas
# Il faut que le nombre soit un nombre entier naturel non nul
# Si tu sais pas c'est quoi, tape "?" ou cherche sur l'internet
# Si tu veux arrêter, tape "stop"



n = ""

def heureux(n):
	if n == "?":
		return "En mathématiques, un entier naturel est un nombre heureux si, lorsqu'on calcule la somme des carrés de ses chiffres dans son écriture en base dix puis la somme des carrés des chiffres du nombre obtenu et ainsi de suite, on aboutit au nombre 1."

	while int(n) != 4 and int(n) != 16 and int(n) != 37 and int(n) != 58 and int(n) != 89 and int(n) != 145 and int(n) != 42 and int(n) != 20 and int(n) != 8 and int(n) != 0:

		x = 0
		for i in list(n):
			x += int(i)**2
		n = str(x)
		print(int(n))

		if int(n) == 1:
			return ("Heureux")
		
	return ("Pas heureux")


while n.upper() != "STOP":
	n = input("Entre un nombre: ")
	if n.upper() == "STOP":
		break
	try:
		print(heureux(n))
	except ValueError:
		print("C'est pas un nombre")



print("Au revoir")
