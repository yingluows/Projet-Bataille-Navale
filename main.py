import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin, Bateau

def generer_placements_possibles(grille, bateau_type):
    """Génère toutes les positions valides (ligne, colonne, orientation) pour placer un bateau."""
    placements_valides = []
    for ligne in range(grille.nombre_lignes):
        for colonne in range(grille.nombre_colonnes):
            for vertical in [True, False]:
                bateau = bateau_type(ligne, colonne, vertical)
                positions = bateau.positions
                if all(0 <= l < grille.nombre_lignes and 0 <= c < grille.nombre_colonnes for (l, c) in positions):
                    # Vérifier chevauchement
                    if all(grille.matrice[l * grille.nombre_colonnes + c] == grille.vide for (l, c) in positions):
                        placements_valides.append((ligne, colonne, vertical))
    return placements_valides

def placer_bateau_aleatoirement(grille, bateau_type):
    placements = generer_placements_possibles(grille, bateau_type)
    if not placements:
        return None
    ligne, colonne, vertical = random.choice(placements)
    bateau = bateau_type(ligne, colonne, vertical)
    grille.ajoute(bateau)
    return bateau

def message_coule(bateau):
    if isinstance(bateau, PorteAvion):
        return "Le porte-avion a été coulé !"
    elif isinstance(bateau, Croiseur):
        return "Le croiseur a coulé sous vos tirs !"
    elif isinstance(bateau, Torpilleur):
        return "Le torpilleur est neutralisé !"
    elif isinstance(bateau, SousMarin):
        return "Le sous-marin a été touché... et coulé !"
    return "Un bateau a été coulé."

def main():
    lignes, colonnes = 8, 10
    grille = Grille(lignes, colonnes)
    bateaux = []

    # Initialiser les 4 bateaux
    for bateau_type in [PorteAvion, Croiseur, Torpilleur, SousMarin]:
        bateau = placer_bateau_aleatoirement(grille, bateau_type)
        if bateau:
            bateaux.append(bateau)

    coups = 0
    bateaux_coules = set()

    while len(bateaux_coules) < len(bateaux):
        print("\nGrille :")
        print(grille)

        try:
            x = int(input("Entrez la colonne (0 à 9) : "))
            y = int(input("Entrez la ligne (0 à 7) : "))
        except ValueError:
            print("Veuillez entrer des entiers valides.")
            continue

        if not (0 <= x < colonnes and 0 <= y < lignes):
            print("Coordonnées hors grille.")
            continue

        coups += 1
        index = y * colonnes + x

        # Vérifier si on touche un bateau
        touche_un_bateau = False
        pour_afficher = None

        for bateau in bateaux:
            if bateau in bateaux_coules:
                continue
            if (y, x) in bateau.positions:
                grille.tirer(y, x, touche='💣')
                touche_un_bateau = True
                if bateau.coulé(grille):
                    bateaux_coules.add(bateau)
                    # Révéler le bateau sur la grille avec sa marque
                    for (l, c) in bateau.positions:
                        grille.tirer(l, c, touche=bateau.marque)
                    print(message_coule(bateau))
                break

        if not touche_un_bateau:
            grille.tirer(y, x, touche='💧')
            print("Plouf !")

    print("\n🎉 Tous les bateaux ont été coulés en", coups, "coups !")
    print("Grille finale :")
    print(grille)

if __name__ == "__main__":
    main()
