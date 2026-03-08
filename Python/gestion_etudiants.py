# gestion_etudiants.py
# Mini système de gestion des étudiants en Python
# Auteur : ...
# Date : Mars 2026

import os  # pour effacer la console (optionnel)

# Liste globale contenant tous les étudiants (chaque étudiant est un dictionnaire)
etudiants = []

# Compteur pour générer automatiquement les IDs (incrémental)
prochain_id = 1

# ----------------------------------------------------------------------
# Fonctions utilitaires de validation
# ----------------------------------------------------------------------

def afficher_titre(titre):
    """Affiche un titre encadré pour une meilleure lisibilité."""
    print("\n" + "=" * 50)
    print(titre.center(50))
    print("=" * 50)

def valider_sexe(s):
    """Vérifie que le sexe est 'M' ou 'F' (insensible à la casse)."""
    return s.upper() in ('M', 'F')

def valider_age(a):
    """Vérifie que l'âge est un entier > 0 et < 150."""
    try:
        age = int(a)
        return 0 < age < 150
    except ValueError:
        return False

def valider_telephone(tel):
    """Vérifie que le téléphone ne contient que des chiffres (bonus)."""
    return tel.isdigit()

def valider_actif(rep):
    """Convertit 'oui'/'non' en booléen, retourne (booléen, erreur)."""
    r = rep.strip().lower()
    if r == 'oui':
        return True, None
    elif r == 'non':
        return False, None
    else:
        return None, "Veuillez saisir 'oui' ou 'non'."

def saisir_entier(message):
    """
    Demande à l'utilisateur de saisir un entier.
    Boucle jusqu'à obtenir une valeur valide (gère les exceptions).
    """
    while True:
        try:
            valeur = int(input(message))
            return valeur
        except ValueError:
            print("❌ Erreur : veuillez entrer un nombre entier valide.")

def trouver_etudiant_par_id(id_cible):
    """
    Parcourt la liste des étudiants et retourne l'étudiant correspondant à l'ID.
    Retourne (étudiant, index) ou (None, -1) si non trouvé.
    """
    for i, etu in enumerate(etudiants):
        if etu['id'] == id_cible:
            return etu, i
    return None, -1

# ----------------------------------------------------------------------
# Fonctions principales du menu
# ----------------------------------------------------------------------

def lister_etudiants():
    """Affiche la liste de tous les étudiants (ID et nom complet)."""
    afficher_titre("LISTE DES ÉTUDIANTS")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    # Utilisation d'une boucle for (obligatoire)
    for etu in etudiants:
        print(f"ID: {etu['id']} | {etu['prenom']} {etu['nom']}")
    print(f"Total : {len(etudiants)} étudiant(s)")

def ajouter_etudiant():
    """Ajoute un nouvel étudiant avec saisie et validation des données."""
    global prochain_id
    afficher_titre("AJOUTER UN ÉTUDIANT")

    # Génération automatique de l'ID
    nouvel_id = prochain_id
    prochain_id += 1

    print(f"ID automatique : {nouvel_id}")

    # Saisie et validation du nom
    nom = input("Nom : ").strip()
    while not nom:
        print("Le nom ne peut pas être vide.")
        nom = input("Nom : ").strip()

    # Saisie et validation du prénom
    prenom = input("Prénom : ").strip()
    while not prenom:
        print("Le prénom ne peut pas être vide.")
        prenom = input("Prénom : ").strip()

    # Saisie et validation du sexe (M/F)
    sexe = input("Sexe (M/F) : ").strip().upper()
    while not valider_sexe(sexe):
        print("Sexe invalide. Veuillez saisir M ou F.")
        sexe = input("Sexe (M/F) : ").strip().upper()

    # Saisie et validation du téléphone (bonus : uniquement des chiffres)
    telephone = input("Téléphone (uniquement des chiffres) : ").strip()
    while not valider_telephone(telephone):
        print("Téléphone invalide. Veuillez saisir uniquement des chiffres.")
        telephone = input("Téléphone : ").strip()

    # Saisie et validation de l'âge (entier, 0 < age < 150)
    age = saisir_entier("Âge : ")
    while not valider_age(age):
        print("Âge invalide. L'âge doit être compris entre 1 et 149.")
        age = saisir_entier("Âge : ")

    # Saisie du niveau (texte libre, mais non vide)
    niveau = input("Niveau (ex: L1, M2, ...) : ").strip()
    while not niveau:
        print("Le niveau ne peut pas être vide.")
        niveau = input("Niveau : ").strip()

    # Saisie et validation de 'actif' (oui/non)
    actif_str = input("Actif (oui/non) : ").strip().lower()
    actif, erreur = valider_actif(actif_str)
    while erreur:
        print(erreur)
        actif_str = input("Actif (oui/non) : ").strip().lower()
        actif, erreur = valider_actif(actif_str)

    # Création du dictionnaire étudiant
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

    # Ajout à la liste
    etudiants.append(nouvel_etudiant)
    print(f"✅ Étudiant ajouté avec succès (ID {nouvel_id}).")

def afficher_etudiant():
    """Affiche les détails d'un étudiant à partir de son ID."""
    afficher_titre("AFFICHER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    id_cible = saisir_entier("Entrez l'ID de l'étudiant : ")
    etu, _ = trouver_etudiant_par_id(id_cible)

    if etu is None:
        print(f"❌ Aucun étudiant trouvé avec l'ID {id_cible}.")
        return

    # Affichage détaillé
    print(f"\nID           : {etu['id']}")
    print(f"Nom          : {etu['nom']}")
    print(f"Prénom       : {etu['prenom']}")
    print(f"Sexe         : {etu['sexe']}")
    print(f"Téléphone    : {etu['telephone']}")
    print(f"Âge          : {etu['age']}")
    print(f"Niveau       : {etu['niveau']}")
    print(f"Actif        : {'Oui' if etu['actif'] else 'Non'}")

def modifier_etudiant():
    """Modifie les informations d'un étudiant existant."""
    afficher_titre("MODIFIER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    id_cible = saisir_entier("Entrez l'ID de l'étudiant à modifier : ")
    etu, index = trouver_etudiant_par_id(id_cible)

    if etu is None:
        print(f"❌ Aucun étudiant trouvé avec l'ID {id_cible}.")
        return

    print("Laissez vide pour conserver la valeur actuelle.")

    # Modification du nom
    nouveau_nom = input(f"Nom [{etu['nom']}] : ").strip()
    if nouveau_nom:
        etu['nom'] = nouveau_nom

    # Modification du prénom
    nouveau_prenom = input(f"Prénom [{etu['prenom']}] : ").strip()
    if nouveau_prenom:
        etu['prenom'] = nouveau_prenom

    # Modification du sexe
    nouveau_sexe = input(f"Sexe (M/F) [{etu['sexe']}] : ").strip().upper()
    if nouveau_sexe:
        while not valider_sexe(nouveau_sexe):
            print("Sexe invalide. Veuillez saisir M ou F.")
            nouveau_sexe = input(f"Sexe (M/F) [{etu['sexe']}] : ").strip().upper()
        etu['sexe'] = nouveau_sexe

    # Modification du téléphone
    nouveau_tel = input(f"Téléphone [{etu['telephone']}] : ").strip()
    if nouveau_tel:
        while not valider_telephone(nouveau_tel):
            print("Téléphone invalide. Uniquement des chiffres.")
            nouveau_tel = input(f"Téléphone [{etu['telephone']}] : ").strip()
        etu['telephone'] = nouveau_tel

    # Modification de l'âge
    nouvel_age = input(f"Âge [{etu['age']}] : ").strip()
    if nouvel_age:
        try:
            age_int = int(nouvel_age)
            while not valider_age(age_int):
                print("Âge invalide. L'âge doit être entre 1 et 149.")
                nouvel_age = input(f"Âge [{etu['age']}] : ").strip()
                age_int = int(nouvel_age)
            etu['age'] = age_int
        except ValueError:
            print("Valeur non numérique, âge inchangé.")

    # Modification du niveau
    nouveau_niveau = input(f"Niveau [{etu['niveau']}] : ").strip()
    if nouveau_niveau:
        etu['niveau'] = nouveau_niveau

    # Modification du statut actif
    nouveau_actif = input(f"Actif (oui/non) [{'oui' if etu['actif'] else 'non'}] : ").strip().lower()
    if nouveau_actif:
        actif, erreur = valider_actif(nouveau_actif)
        while erreur:
            print(erreur)
            nouveau_actif = input(f"Actif (oui/non) [{'oui' if etu['actif'] else 'non'}] : ").strip().lower()
            actif, erreur = valider_actif(nouveau_actif)
        etu['actif'] = actif

    print(f"✅ Étudiant ID {id_cible} modifié avec succès.")

def supprimer_etudiant():
    """Supprime un étudiant de la liste."""
    afficher_titre("SUPPRIMER UN ÉTUDIANT")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    id_cible = saisir_entier("Entrez l'ID de l'étudiant à supprimer : ")
    etu, index = trouver_etudiant_par_id(id_cible)

    if etu is None:
        print(f"❌ Aucun étudiant trouvé avec l'ID {id_cible}.")
        return

    # Confirmation
    conf = input(f"Voulez-vous vraiment supprimer {etu['prenom']} {etu['nom']} (ID {id_cible}) ? (o/n) : ").strip().lower()
    if conf == 'o':
        del etudiants[index]
        print(f"✅ Étudiant ID {id_cible} supprimé.")
    else:
        print("Suppression annulée.")

def rechercher_par_nom():
    """Bonus : recherche les étudiants dont le nom ou prénom contient une chaîne."""
    afficher_titre("RECHERCHE PAR NOM/PRÉNOM")
    if not etudiants:
        print("Aucun étudiant enregistré.")
        return

    terme = input("Entrez un nom ou prénom (ou partie) : ").strip().lower()
    if not terme:
        print("Terme de recherche vide.")
        return

    resultats = []
    for etu in etudiants:
        if terme in etu['nom'].lower() or terme in etu['prenom'].lower():
            resultats.append(etu)

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
    """Boucle principale du menu."""
    while True:
        # Affichage du menu
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

        # Gestion des options
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
            print("❌ Option invalide. Veuillez choisir un nombre entre 1 et 7.")

        # Pause pour permettre à l'utilisateur de lire les résultats
        input("\nAppuyez sur Entrée pour continuer...")
        # Effacer la console (optionnel, commenter si non désiré)
        # os.system('cls' if os.name == 'nt' else 'clear')

# Point d'entrée du programme
if __name__ == "__main__":
    main()