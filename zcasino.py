import random
import math

def miser(mise): # test format et mise positive et mise > bank
	try:
		mise = int(mise)
		assert mise > 0 and bank - mise >= 0
	except ValueError:
		return False
	except AssertionError:
		return False
	else:
		return True

def choix_num(num): # test format et compris entre 0 et 49
	try:
		num = int(num)
		assert num >= 0 and num <= 49
	except ValueError:
		return False
	except AssertionError:
		return False
	else:
		return True

def num_pair(num_a_tester): # test nombre pair/impair
	if num_a_tester%2 == 0:
		return True
	else:
		return False
	
print("WELCOME to Zcasino") # message de bienvenu
bank = 100	# banque de départ 100$
print("Bank: $", bank)

while bank > 0:
	num = input("Choisir Numéro entre 0 et 49 :") # le joueur choisit son numéro
	while choix_num(num) == False:
		print("numéro non valide")
		num = input("Choisir Numéro entre 0 et 49 :")
		choix_num(num)
	else:
		num_choisi = int(num)

	mise = input("mise: $") # le joueur mise
	while miser(mise) == False:
		print("mise non valide")
		mise = input("mise: $")
		miser(mise)
	else:
		bank = bank - int(mise)

	num_sorti = random.randrange(50) # la roue tourne et tombe sur le:
	print("La roue a choisit le :", num_sorti)
	print("Et tu as misé sur le :", num_choisi)

	if num_choisi == num_sorti: # si les num sont les mêmes
		gain = int(mise) * 3
		print("JACKPOT!!!  gain : $", gain)
		bank = int(bank) + int(mise) + int(gain) # j gagne mise + mise x 3
		print("Bank : $", bank)
	elif num_pair(num_choisi) == num_pair(num_sorti):
		gain = int(mise) / 2
		print("GAGNE!!!  gain : $", math.ceil(gain))
		bank = int(bank) + int(mise) + math.ceil(gain)
		print("Bank : $", bank)
	else:
		print("PERDU!!!!  gain : $0")
		bank = bank
		print("Bank : $", bank)

else:
	print("BANKROUT")

	


# si les num ont la même couleur -> j gagne mise + mise/2(arrondi entier sup)
# si les ni l'un ni l'autre -> j perd sa mise
# le jeu se termine quand la banque est à 0 -> BANKROUT