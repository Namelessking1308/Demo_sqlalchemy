from .base import Base
from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class DetailJeu(Base):

    __tablename__ = "details_jeux"

    jeu_id = Column(
        Integer, ForeignKey("jeux.jeu_id"),
        primary_key = True
    )

    description = Column(Text)
    note_metacritic = Column(Integer)
    multijoueur = Column(Boolean, default = False)

    jeu = relationship("Jeu", back_populates = "details")