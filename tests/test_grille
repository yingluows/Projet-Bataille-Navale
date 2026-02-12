from bateau import Bateau
from grille import Grille

def test_init():
    g = Grille(5, 8)
    assert g.nombre_lignes == 5
    assert g.nombre_colonnes == 8
    assert len(g.matrice) == 5 * 8
    assert all(c == g.vide for c in g.matrice)

def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3) 
    index = 2 * g.nombre_colonnes + 3
    assert g.matrice[index] == g.touche

def test_affichage():
    g = Grille(3, 4)
    # avant tir
    attendu_avant = "∿∿∿∿\n∿∿∿∿\n∿∿∿∿"
    assert str(g) == attendu_avant

    # après tir
    g.tirer(1, 2)
    attendu_apres = "∿∿∿∿\n∿∿x∿\n∿∿∿∿"
    assert str(g) == attendu_apres

def test_ajoute_bateau_dans_grille():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)  
    g.ajoute(b)
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

def test_bateau_depasse_vertical():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=True)  
    g.ajoute(b)
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]

def test_bateau_trop_long():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=4, vertical=True)  
    g.ajoute(b)
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]  

def test_tir_personnalise():
    g = Grille(2, 3)
    g.tirer(0, 1, touche='💥')
    index = 0 * g.nombre_colonnes + 1
    assert g.matrice[index] == '💥'

