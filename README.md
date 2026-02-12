# Projet-Bataille-Navale
Projet "Bataille Navale" réalisé dans le cadre de l’approfondissement MIE Info 1.   Développé par Tianle Cheng.

# Bataille Navale 

## Description

Un jeu de bataille navale en ligne de commande, en Python.  
Placez des bateaux aléatoirement, tirez sur la grille, coulez-les tous !

---

## Lancer le jeu

### 1. Créer l'environnement virtuel

python -m venv venv


### 2. Activer l’environnement virtuel

Windows :

venv\Scripts\activate

macOS / Linux :

source venv/bin/activate


### 3. Installer les dépendances

pip install -r requirements.txt


### 4. Lancer le jeu

python main.py


Suivez les instructions dans le terminal pour tirer sur la grille, découvrir et couler tous les bateaux ennemis.

---

## Lancer les tests

pytest


---

## Structure du projet

bataille-navale/
├── main.py
├── grille.py
├── bateau.py
├── story_grille.py
├── story_bateau.py
├── requirements.txt
├── .gitignore
├── README.md
└── tests/
├── test_grille.py
└── test_bateau.py
