from .base import Base
from .jeu import Jeu
from .detail_jeu import DetailJeu
from .developpeur import Developpeur
from .plateforme import Plateforme
from sqlalchemy import Table, Column, Integer, String, ForeignKey

__all__ = [
    "Base",
    "Jeu",
    "DetailJeu",
    "Developpeur",
    "Plateforme"
]

jeux_plateformes = Table(
    "jeux_plateformes",
    Base.metadata,
    Column("jeu_id", Integer, ForeignKey("jeux.jeu_id"), primary_key = True),
    Column("plateforme_id", Integer, ForeignKey("plateformes.plateforme_id"), primary_key = True)
)