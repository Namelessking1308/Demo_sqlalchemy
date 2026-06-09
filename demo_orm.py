from dal.models import Jeu, DetailJeu, Developpeur
from dal.database import get_session, init_db, test_connection

def main():
    print("=" * 20)

    if not test_connection():
        return

    init_db()

    print("=" * 20)

if __name__ == "__main__":
    main()