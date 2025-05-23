from pathlib import Path
from tinydb import TinyDB, Query


class Tache:
	BASE_DIR = Path(__file__).parent.resolve()
	DB = TinyDB(BASE_DIR / "datas" / "taches.json")
	CHECK_DB = Query()
	def __init__(self, titre: str, etat: bool=False):
		self.titre = titre.lower()
		self.etat = etat

	def __repr__(self):
		return f"Tache(titre={self.titre.title()}, etat={self.etat})"

	def __str__(self):
		to_do = "[ ]" if not self.etat else "[X]"
		return f"{to_do} : {self.titre.title()}"

	def sauvegarder_tache(self):
		# self.check_db_file_exists()

		if self.DB.search(self.CHECK_DB.titre==self.titre):
			return -1
		else:
			return self.DB.insert(self.__dict__)

	def supprimer_tache(self):
		# self.check_db_file_exists()
		if not self.DB.search(self.CHECK_DB.titre==self.titre):
			return [-1]
		else:
			return self.DB.remove(self.CHECK_DB.titre==self.titre)


	def check_db_file_exists(self): #NE FONCTIONNE PAS, A REVOIR
		db_file = self.BASE_DIR / "datas" / "taches.json"
		try:
			self.BASE_DIR.mkdir()
		except FileExistsError:
			print("Le dossier 'datas/' existe déjà, action mkdir() ignorée.")
		try:
			db_file.touch()
		except FileExistsError:
			print("Le fichier 'taches.json' existe déjà, action touch() ignorée.")

	def cocher_tache(self):
		self.etat = True
		self.DB.update({"etat" : True}, self.CHECK_DB.titre==self.titre)
		return self.etat

	def decocher_tache(self):
		self.etat = False
		self.DB.update({"etat" : False}, self.CHECK_DB.titre==self.titre)
		return self.etat


def get_all_taches():
	# Tache.check_db_file_exists()
	all_taches = []
	for tache in Tache.DB.all():
		all_taches.append(Tache(titre=tache["titre"], etat=tache["etat"]))
	return all_taches





if __name__ == "__main__":
	test = Tache(titre="Blabla blabla", etat=False)
	test2 = Tache(titre="Faire la sieste", etat=True)

	test.sauvegarder_tache()
	test2.sauvegarder_tache()

