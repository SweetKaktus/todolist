import os
import sys

from tache import Tache, get_all_taches

def main():
	poursuivre = ""
	choix = ""
	all_taches = get_all_taches()
	while not choix:
		all_taches = get_all_taches()
		clear()
		print_main_title()
		print("Votre To Do List:")
		for i, t in enumerate(all_taches, start=1):
			print(f"{i}. {t}")
		print()
		print("Que voulez-vous faire ?\n1. Ajouter une tache\n2. Cocher une tache\n3. Decocher une tache\n4. Supprimer une tache\n5. Quitter")
	
		choix = input("Saisissez un numéro (1/2/3/4/5)\n")
		match choix:
			case "1":
				nouvelle_tache = Tache(titre=input("Saisissez un nom de tache:\n"))
				nouvelle_tache.sauvegarder_tache()
				print(f"La tache {nouvelle_tache.titre.title()} a ete creee")
				choix = ""
			case "2":
				tache_a_cocher = input("Saisissez le numero de la tache a cocher:\n")
				for i, t in enumerate(all_taches, start=1):
					if str(i) == tache_a_cocher:
						t.cocher_tache()
						print(f"La tache {t.titre.title()} a ete cochee")
						t.sauvegarder_tache()
					else:
						print(f"{t}")
				choix = ""
				input()
			case "3":
				tache_a_decocher = input("Saisissez le nom de la tache a decocher:\n")
				for i, t in enumerate(all_taches, start=1):
					if str(i) == tache_a_decocher:
						t.decocher_tache()
						print(f"La tache {t.titre.title()} a ete decochee")
						t.sauvegarder_tache()
				choix = ""
				input()
			case "4":
				tache_supprimer = input("Saissiez le numero de la tache a supprimer:\n")
				for i, t in enumerate(all_taches, start=1):
					if str(i) == tache_supprimer:
						t.supprimer_tache()
						print(f"La tache {t.titre.title()} a ete supprimee.")
				choix = ""
				input()
			case "5":
				print("Merci et à bientot !")
				input()
				sys.exit()
			case _:
				choix = ""
				input("Je n'ai pas compris.")


def print_main_title():
	print(("#" * 24)+"\n"+"#"+(" " * 22)+"#\n#      TO DO LIST      #\n#"+(" " * 22)+"#\n"+("#" * 24))


def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")



if __name__ == "__main__":
	main()