# Système de Gestion des étudiants
# Auteur : Crawford (GHOST)
# Date : Mars 2026

import os

# Liste des étudiants (chaque étudiant est un dictionnaire)
etudiants = []
prochain_id = 1

# ----------------------------------------------------------------------
# Fonctions d'affichage et utilitaires
# ----------------------------------------------------------------------

def afficher_titre(titre):
    """Affiche un titre encadré."""
    print("\n" + "=" * 50)
    print(titre.center(50))
    print("=" * 50)

def saisir_entier(message):
    """Demande un entier à l'utilisateur avec gestion d'erreur."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier valide.")

def trouver_etudiant_par_id(id_cible):
    """Recherche un étudiant par son ID. Retourne (étudiant, index) ou (None, -1)."""
    for i, etu in enumerate(etudiants):
        if etu['id'] == id_cible:
            return etu, i
    return None, -1

# ----------------------------------------------------------------------
# Fonctions de saisie avec validation intégrée
# ----------------------------------------------------------------------

def saisir_sexe():
    """Demande et valide le sexe (M/F)."""
    while True:
        s = input("Sexe (M/F) : ").strip().upper()
        if s in ('M', 'F'):
            return s
        print("Sexe invalide. Veuillez saisir M ou F.")

def saisir_telephone():
    """Demande et valide le téléphone (uniquement des chiffres)."""
    while True:
        tel = input("Téléphone (uniquement des chiffres) : ").strip()
        if tel.isdigit():
            return tel
        print("Téléphone invalide. Utilisez uniquement des chiffres.")

def saisir_age():
    """Demande et valide l'âge (1-99)."""
    while True:
        age = saisir_entier("Âge : ")
        if 1 <= age <= 99:
            return age
        print("Âge invalide. L'âge doit être compris entre 1 et 99.")

def saisir_actif():
    """Demande et valide le statut actif (oui/non) et retourne un booléen."""
    while True:
        rep = input("Actif (Oui/Non) : ").strip().lower()
        if rep == 'oui':
            return True
        elif rep == 'non':
            return False
        print("Veuillez saisir 'Oui' ou 'Non'.")

# ----------------------------------------------------------------------
# Fonctions principales du menu
# ----------------------------------------------------------------------

def lister_etudiants():
    afficher_titre("LISTE DES ÉTUDIANTS")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    for etu in etudiants:
        print(f"ID: {etu['id']} | {etu['prenom']} {etu['nom']}")
    print(f"Total : {len(etudiants)} étudiant(s)")

def ajouter_etudiant():
    global prochain_id
    afficher_titre("AJOUTER UN ÉTUDIANT")
    nouvel_id = prochain_id
    prochain_id += 1
    print(f"ID automatique : {nouvel_id}")

    # Saisies avec validation
    nom = input("Nom : ").strip()
    while not nom:
        print("Le nom ne peut pas être vide.")
        nom = input("Nom : ").strip()

    prenom = input("Prénom : ").strip()
    while not prenom:
        print("Le prénom ne peut pas être vide.")
        prenom = input("Prénom : ").strip()

    sexe = saisir_sexe()
    telephone = saisir_telephone()
    age = saisir_age()

    niveau = input("Niveau (ex: L1, M2, ...) : ").strip()
    while not niveau:
        print("Le niveau ne peut pas être vide.")
        niveau = input("Niveau : ").strip()

    actif = saisir_actif()

    # Création de l'étudiant
    nouvel_etudiant = {
        'id': nouvel_id,
        'nom': nom,
        'prenom': prenom,
        'sexe': sexe,
        'telephone': telephone,
        'age': age,
        'niveau': niveau,
        'actif': actif
    }
    etudiants.append(nouvel_etudiant)
    print(f"Étudiant ajouté avec succès (ID {nouvel_id}).")

def afficher_etudiant():
    afficher_titre("AFFICHER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    id_cible = saisir_entier("Entrez l'ID de l'étudiant : ")
    etu, _ = trouver_etudiant_par_id(id_cible)
    if etu is None:
        print(f"Aucun étudiant trouvé avec l'ID {id_cible}.")
        return
    print(f"\nID           : {etu['id']}")
    print(f"Nom          : {etu['nom']}")
    print(f"Prénom       : {etu['prenom']}")
    print(f"Sexe         : {etu['sexe']}")
    print(f"Téléphone    : {etu['telephone']}")
    print(f"Âge          : {etu['age']}")
    print(f"Niveau       : {etu['niveau']}")
    print(f"Actif        : {'Oui' if etu['actif'] else 'Non'}")

def modifier_etudiant():
    afficher_titre("MODIFIER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    id_cible = saisir_entier("Entrez l'ID de l'étudiant à modifier : ")
    etu, _ = trouver_etudiant_par_id(id_cible)
    if etu is None:
        print(f"Aucun étudiant trouvé avec l'ID {id_cible}.")
        return

    print("Laissez vide pour conserver la valeur actuelle.")

    # Nom
    nouveau = input(f"Nom [{etu['nom']}] : ").strip()
    if nouveau:
        etu['nom'] = nouveau

    # Prénom
    nouveau = input(f"Prénom [{etu['prenom']}] : ").strip()
    if nouveau:
        etu['prenom'] = nouveau

    # Sexe
    nouveau = input(f"Sexe (M/F) [{etu['sexe']}] : ").strip().upper()
    if nouveau:
        while nouveau not in ('M', 'F'):
            print("Sexe invalide. Veuillez saisir M ou F.")
            nouveau = input(f"Sexe (M/F) [{etu['sexe']}] : ").strip().upper()
        etu['sexe'] = nouveau

    # Téléphone
    nouveau = input(f"Téléphone [{etu['telephone']}] : ").strip()
    if nouveau:
        while not nouveau.isdigit():
            print("Téléphone invalide. Uniquement des chiffres.")
            nouveau = input(f"Téléphone [{etu['telephone']}] : ").strip()
        etu['telephone'] = nouveau

    # Âge
    nouvel_age = input(f"Âge [{etu['age']}] : ").strip()
    if nouvel_age:
        try:
            age_int = int(nouvel_age)
            while not (1 <= age_int <= 99):
                print("Âge invalide. L'âge doit être entre 1 et 99.")
                nouvel_age = input(f"Âge [{etu['age']}] : ").strip()
                age_int = int(nouvel_age)
            etu['age'] = age_int
        except ValueError:
            print("Valeur non numérique, âge inchangé.")

    # Niveau
    nouveau = input(f"Niveau [{etu['niveau']}] : ").strip()
    if nouveau:
        etu['niveau'] = nouveau

    # Actif
    nouveau = input(f"Actif (Oui/Non) [{'Oui' if etu['actif'] else 'Non'}] : ").strip().lower()
    if nouveau:
        while nouveau not in ('oui', 'non'):
            print("Veuillez saisir 'Oui' ou 'Non'.")
            nouveau = input(f"Actif (Oui/Non) [{'Oui' if etu['actif'] else 'Non'}] : ").strip().lower()
        etu['actif'] = (nouveau == 'oui')

    print(f"Étudiant ID {id_cible} modifié avec succès.")

def supprimer_etudiant():
    afficher_titre("SUPPRIMER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    id_cible = saisir_entier("Entrez l'ID de l'étudiant à supprimer : ")
    etu, index = trouver_etudiant_par_id(id_cible)
    if etu is None:
        print(f"Aucun étudiant trouvé avec l'ID {id_cible}.")
        return
    conf = input(f"Voulez-vous vraiment supprimer {etu['prenom']} {etu['nom']} (ID {id_cible}) ? (O/N) : ").strip().lower()
    if conf == 'o':
        del etudiants[index]
        print(f"Étudiant ID {id_cible} supprimé.")
    else:
        print("Suppression annulée.")

def rechercher_par_nom():
    afficher_titre("RECHERCHE PAR NOM/PRÉNOM")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return
    terme = input("Entrez un nom ou prénom (ou partie) : ").strip().lower()
    if not terme:
        print("Terme de recherche vide.")
        return
    resultats = [etu for etu in etudiants if terme in etu['nom'].lower() or terme in etu['prenom'].lower()]
    if not resultats:
        print("Aucun étudiant correspondant.")
    else:
        print(f"{len(resultats)} résultat(s) trouvé(s) :")
        for etu in resultats:
            print(f"ID: {etu['id']} | {etu['prenom']} {etu['nom']} (Actif: {'Oui' if etu['actif'] else 'Non'})")

# ----------------------------------------------------------------------
# Programme principal
# ----------------------------------------------------------------------

def main():
    while True:
        print("\n" + "=" * 50)
        print(" MENU PRINCIPAL - GESTION DES ÉTUDIANTS".center(50))
        print("=" * 50)
        print("1 - Lister les étudiants")
        print("2 - Ajouter un étudiant")
        print("3 - Afficher un étudiant")
        print("4 - Modifier un étudiant")
        print("5 - Supprimer un étudiant")
        print("6 - Rechercher par nom (bonus)")
        print("7 - Fermer le programme")
        print("-" * 50)

        choix = input("Votre choix : ").strip()

        if choix == '1':
            lister_etudiants()
        elif choix == '2':
            ajouter_etudiant()
        elif choix == '3':
            afficher_etudiant()
        elif choix == '4':
            modifier_etudiant()
        elif choix == '5':
            supprimer_etudiant()
        elif choix == '6':
            rechercher_par_nom()
        elif choix == '7':
            print("Fermeture du programme. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir un nombre entre 1 et 7.")

        input("\nAppuyez sur Entrée pour continuer...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()