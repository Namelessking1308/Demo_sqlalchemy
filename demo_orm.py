from datetime import date, datetime
from decimal import Decimal
from dal.models import Jeu, DetailJeu, Developpeur, Plateforme
from dal.database import get_session, init_db, test_connection
from sqlalchemy.orm import joinedload

def seed(session):
    # Création d'un dev
    nintendo = Developpeur(
        nom = "Nintendo",
        pays = "Japon"
    )
    session.add(nintendo)
    session.flush()     # pour obtenir mon id

    # Création d'un jeu avec ses relations
    pokemon = Jeu(
        titre = "Pokemon",
        date_sortie = date(2027, 3, 15),
        prix = Decimal("59.99"),
        developpeur = nintendo
    )

    pokemon.details = DetailJeu(
        description = "Jeu de monstre",
        note_metacritic = 2,
        multijoueur = True
    )

    switch = Plateforme(
        nom = "Switch",
        fabricant = "Nintendo"
    )
    pokemon.plateformes.append(switch)

    session.add(pokemon)
    session.commit()
    print("Données initales crées avec succès !")

def lire_jeux(session):
    jeux = session.query(Jeu).options(
        joinedload(Jeu.developpeur),
        joinedload(Jeu.details),
        joinedload(Jeu.plateformes)
    ).all()

    for jeu in jeux:
        print(f"\n{jeu.titre} (ID: {jeu.jeu_id})")
        print(f"   => Développeur      : {jeu.developpeur.nom if jeu.developpeur else 'N/A'}")
        print(f"   => Prix              : {jeu.prix}€")
        print(f"   => Note Metacritic      : {jeu.details.note_metacritic}/20")
        print(f"   => Plateforme(s)      : {[p.nom for p in jeu.plateformes]}")


def creer_jeux(session):

        titre = input("Entrer le titre du jeu: ")
        date_jeu = datetime.strptime(input("Entrer la date de sortie du jeu: "), "%Y-%m-%d").date()
        prix = Decimal(input("Entrer le prix du jeu: "))
        nom_dev = input("Entrer le nom du developpeur: ")
        pays = input("Entrer le pays du developpeur: ")
        description_jeu = input("Entrer une déscription du jeu: ")
        note_jeu = int(input("Entrez une note /20: "))
        multi = input("Est-ce un jeu multijoueur ? (o/n) ").lower()
        nom_console = input("Entrez une plateforme pour le jeu: ")
        fabricant_console = input("Entrez le fabriquant de la console: ")

        developpeur = Developpeur(
            nom = nom_dev,
            pays = pays
        )

        jeu = Jeu(
            titre = titre,
            date_sortie = date_jeu,
            prix = prix,
            developpeur = developpeur
        )
        session.add(jeu)
        session.commit()
        print("Nouveau jeu créer avec succès !")

        jeu.details = DetailJeu(
            description = description_jeu,
            note_metacritic = note_jeu,
            multijoueur = multi if multi == "o" else False
        )

        console = Plateforme(
            nom = nom_console,
            fabricant = fabricant_console
        )

        jeu.plateformes.append(console)

def mettre_a_jour(session):
    pass

def supprimer(session):
    pass


def main():
    if not test_connection():
        return

    session = get_session()

    init_db(delete = True)
    seed(session)

    retry = True
    while retry:
        print("\n" + "*" * 50)

        print("MENU CRUD")
        print("*" * 30)
        print("[1] Lister tout les jeux")
        print("[2] Créer un nouveau jeu")
        print("[3] Modifier un jeu")
        print("[4] Supprimer un jeu")
        print("[5] Reset (drop + create)")
        print("[0] Quitter")
        print("*" * 30)

        choix = int(input("\nVotre choix : "))

        if choix == 1:
            lire_jeux(session)
        elif choix == 2:
            creer_jeux(session)
        elif choix == 3:
            mettre_a_jour(session)
        elif choix == 4:
            supprimer(session)
        elif choix == 5:
            validation = input("Réinitaliser toutes les tables ? (o/n)").lower()
            if validation == "o":
                init_db(delete = True)
                seed(session)
        elif choix == 0:
            print("Bye Bye !!!")
            retry = False
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()