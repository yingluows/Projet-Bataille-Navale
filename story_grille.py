from grille import Grille

def demander_coordonnees():
    """Demande les coordonnées au joueur, en les validant."""
    try:
        x = int(input("Entrez la colonne (x, de 0 à 7) : "))
        y = int(input("Entrez la ligne (y, de 0 à 4) : "))
        return x, y
    except ValueError:
        print("Entrée invalide, veuillez entrer des entiers.")
        return None, None

def main():
    g = Grille(5, 8) 

    while True:
        print("\nGrille :")
        print(g)
        x, y = demander_coordonnees()
        if x is not None and y is not None:
            g.tirer(y, x)  

if __name__ == "__main__":
    main()
