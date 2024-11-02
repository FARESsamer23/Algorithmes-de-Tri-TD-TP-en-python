class Noeud:
    def __init__(self, cle):
        self.cle = cle
        self.gauche = None
        self.droite = None

class ArbreBinaireDeRecherche:
    def __init__(self):
        self.racine = None

    # Insertion dans l'arbre
    def inserer(self, cle):
        if self.racine is None:
            self.racine = Noeud(cle)
        else:
            self._inserer_recursif(self.racine, cle)

    def _inserer_recursif(self, noeud, cle):
        if cle < noeud.cle:
            if noeud.gauche is None:
                noeud.gauche = Noeud(cle)
            else:
                self._inserer_recursif(noeud.gauche, cle)
        elif cle > noeud.cle:
            if noeud.droite is None:
                noeud.droite = Noeud(cle)
            else:
                self._inserer_recursif(noeud.droite, cle)

    # Recherche dans l'arbre
    def rechercher(self, cle):
        return self._rechercher_recursif(self.racine, cle)

    def _rechercher_recursif(self, noeud, cle):
        if noeud is None or noeud.cle == cle:
            return noeud
        if cle < noeud.cle:
            return self._rechercher_recursif(noeud.gauche, cle)
        return self._rechercher_recursif(noeud.droite, cle)

    # Suppression dans l'arbre
    def supprimer(self, cle):
        self.racine = self._supprimer_recursif(self.racine, cle)

    def _supprimer_recursif(self, noeud, cle):
        if noeud is None:
            return noeud

        if cle < noeud.cle:
            noeud.gauche = self._supprimer_recursif(noeud.gauche, cle)
        elif cle > noeud.cle:
            noeud.droite = self._supprimer_recursif(noeud.droite, cle)
        else:
            # Pas d'enfant ou un seul enfant
            if noeud.gauche is None:
                return noeud.droite
            elif noeud.droite is None:
                return noeud.gauche

            # Noeud avec deux enfants
            min_noeud_plus_grand = self._trouver_min(noeud.droite)
            noeud.cle = min_noeud_plus_grand.cle
            noeud.droite = self._supprimer_recursif(noeud.droite, min_noeud_plus_grand.cle)

        return noeud

    def _trouver_min(self, noeud):
        courant = noeud
        while courant.gauche is not None:
            courant = courant.gauche
        return courant

    # Parcours en ordre croissant (in-order)
    def parcours_en_ordre(self):
        resultat = []
        self._parcours_en_ordre_recursif(self.racine, resultat)
        return resultat

    def _parcours_en_ordre_recursif(self, noeud, resultat):
        if noeud:
            self._parcours_en_ordre_recursif(noeud.gauche, resultat)
            resultat.append(noeud.cle)
            self._parcours_en_ordre_recursif(noeud.droite, resultat)

# Exemple d'utilisation
abr = ArbreBinaireDeRecherche()
abr.inserer(50)
abr.inserer(30)
abr.inserer(20)
abr.inserer(40)
abr.inserer(70)
abr.inserer(60)
abr.inserer(80)

print("Parcours en ordre croissant :", abr.parcours_en_ordre())  # Affiche les valeurs en ordre croissant

# Recherche
noeud = abr.rechercher(40)
print("Recherche du noeud 40 :", "Trouvé" if noeud else "Non trouvé")

# Suppression
abr.supprimer(20)
print("Parcours en ordre croissant après suppression de 20 :", abr.parcours_en_ordre())
