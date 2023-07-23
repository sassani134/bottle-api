from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import random

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def lvl_up():
    lvl += 1
    expMax *= 3
    hp +=random.randrange(0,6,5)
    mp +=random.randrange(0,6,5)
    spd +=random.randrange(0,6,5)


@app.get("/")
async def root():
    return "player"


@app.post("/player", response_model=schemas.Player, status_code=status.HTTP_201_CREATED)
async def create_player(player: schemas.PlayerCreate, session: Session = Depends(get_session)):

    # create an instance of the Player database model
    playerdb = models.Player(name = player.name)

    # add it to the session and commit it
    session.add(playerdb)
    session.commit()
    session.refresh(playerdb)

    # return the player object
    return playerdb


@app.get("/player/{id}", response_model=schemas.Player)
def read_player(id: int, session: Session = Depends(get_session)):

    # get the player item with the given id
    player = session.query(models.Player).get(id)

    # check if player item with given id exists. If not, raise exception and return 404 not found response
    if not player:
        raise HTTPException(status_code=404, detail=f"player  with id {id} not found")

    return player


@app.get("/player/{name}", response_model=schemas.Player)
def read_player(name: str, session: Session = Depends(get_session)):

    # get the player  with the given id
    player = session.query(models.Player).get(name)

    # check if player item with given id exists. If not, raise exception and return 404 not found response
    if not player:
        raise HTTPException(status_code=404, detail=f"player  with name {name} not found")

    return player


@app.put("/player/{id}", response_model=schemas.Player)
def update_player(id: int, task: str, session: Session = Depends(get_session)):

    # get the player item with the given id
    player = session.query(models.Player).get(id)

    # update player item with the given task (if an item with the given id was found)
    if player:
        player.name = name
        session.commit()

    # check if player item with given id exists. If not, raise exception and return 404 not found response
    if not player:
        raise HTTPException(status_code=404, detail=f"player with id {id} not found")

    return player


@app.delete("/player/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(id: int, session: Session = Depends(get_session)):

    # get the player item with the given id
    player = session.query(models.Player).get(id)

    # if player item with given id exists, delete it from the database. Otherwise raise 404 error
    if player:
        session.delete(player)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"player item with id {id} not found")

    return None


@app.get("/players", response_model = List[schemas.Player])
def read_player_list(session: Session = Depends(get_session)):

    # get all player items
    player_list = session.query(models.Player).all()

    return player_list