import pytest
from tache import Tache

from tinydb import TinyDB, Query

from tinydb.storages import MemoryStorage

@pytest.fixture
def setup_db():
	Tache.DB = TinyDB(storage=MemoryStorage)

@pytest.fixture
def tache(setup_db):
	t = Tache(titre="tache pour les tests", etat=False)
	t.sauvegarder_tache()
	return t

def test_sauvegarder_tache(setup_db):
	t = Tache(titre="tache pour le test de sauvegarde", etat=False)
	assert t.sauvegarder_tache() == 1

def test_sauvegarder_tache_twice(tache):
	t = tache
	assert t.sauvegarder_tache() == -1

def test_supprimer_tache(tache):
	assert tache.supprimer_tache() == [1]

def test_supprimer_tache_existe_pas(setup_db):
	t = Tache(titre="tache pour le test de sauvegarde", etat=False)
	assert t.supprimer_tache() == [-1]


def test_cocher_tache(tache):
	t = tache
	assert t.cocher_tache() == True

def test_decocher_tache(tache):
	t = tache
	assert t.decocher_tache() == False