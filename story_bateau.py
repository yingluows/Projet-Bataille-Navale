from bateau import Bateau

def chevauchent(b1, b2):
    """Retourne True si les deux bateaux se chevauchent."""
    return len(set(b1.positions) & set(b2.positions)) > 0

def main():
    print("=== TEST 1 : bateaux qui se chevauchent ===")
    b1 = Bateau(2, 3, longueur=3)           
    b2 = Bateau(2, 4, longueur=2, vertical=False)  
    print("b1 :", b1.positions)
    print("b2 :", b2.positions)
    print("Se chevauchent ?", chevauchent(b1, b2))  # Doit être True

    print("\n=== TEST 2 : bateaux séparés ===")
    b3 = Bateau(0, 0, longueur=2)
    b4 = Bateau(3, 3, longueur=2, vertical=True)
    print("b3 :", b3.positions)
    print("b4 :", b4.positions)
    print("Se chevauchent ?", chevauchent(b3, b4))  # Doit être False

if __name__ == "__main__":
    main()
