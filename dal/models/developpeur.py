"""

Modèle developpeur

Relation : One-to-Many

un développeur peut créer plusieurs jeux.
un jeux n'a qu'un seul développeur

En SQL Alchemy :
-Coté "1" Dev : on utilise relationship() avec une liste
-Coté "N" Jeu : on utilise relationship() + ForeignKey
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Developpeur(Base):
    __tablename__ = "developpeurs"

    developpeur_id = Column(Integer, primary_key = True, autoincrement = True)
    nom = Column(String(100), nullable = False, unique = True)
    pays = Column(String(50))

    # back_populates ==> Permet d'établir la relation en sens inverse (cible le fichier et non pas la class)

    jeux = relationship("Jeu", back_populates = "developpeur")