class Grille:

    def __init__(self, nombre_lignes, nombre_colonnes):
        """Crée une grille vide avec les dimensions données."""
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes
        self.vide = '∿'  
        self.touche = 'x'  
        self.bateau = '⛵'
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def tirer(self, ligne, colonne, touche='x'):
        """Effectue un tir sur la case donnée, et marque le caractère spécifié."""
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            self.matrice[index] = touche


    def ajoute(self, bateau):
        positions = bateau.positions
        for (l, c) in positions:
            if not (0 <= l < self.nombre_lignes and 0 <= c < self.nombre_colonnes):
                return  

        for (l, c) in positions:
            index = l * self.nombre_colonnes + c
            self.matrice[index] = bateau.marque  

    def __str__(self):
        """Retourne une représentation textuelle de la grille."""
        lignes = []
        for l in range(self.nombre_lignes):
            ligne = "".join(
                self.matrice[l * self.nombre_colonnes : (l + 1) * self.nombre_colonnes]
            )
            lignes.append(ligne)
        return "\n".join(lignes)
