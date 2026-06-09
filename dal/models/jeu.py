from .base import Base
from sqlalchemy import Column, Integer, Text, String, Date, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Jeu(Base):
    __tablename__ = "jeux"

    jeu_id = Column(Integer, primary_key = True, autoincrement = True)
    titre = Column(String(200), nullable = False)
    date_sortie = Column(Date)
    prix = Column(DECIMAL(10,2))

    details = relationship("DetailJeu", back_populates = "jeu", uselist = False)