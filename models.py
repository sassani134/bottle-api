from sqlalchemy import Column, Integer, String
from database import Base


# Define To Do class inheriting from Base
class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    lvl = Column(Integer)
    expMax = Column(Integer)
    expCurr = Column(Integer)
    hp = Column(Integer)
    mp = Column(Integer)
    atk = Column(Integer)
    defn = Column(Integer)
    spd = Column(Integer)

