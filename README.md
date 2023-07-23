# Bottle API

## Functionalities

- initialize a Player from Lvl 1
- Read Players
- Read Player Stats
- Update:
  - Update Player Exp, Level, and Stats
  - update Player name
- Delete Player

### Player stats
{
  "name": "Player Name",
  "level": 1,
  "exp": 0,
  "expMax": 100,
  "stats": {
    "hp": 10,
    "attack": 1,
    "defense": 1,
    "speed": 5
  }
}

## Routes
fonctionnalités | method | Chemin |
--- | --- | --- |
Creer un Player | POST | /players
Lire tous les Players | GET | /players
Lire un Player | GET | /players/{id}
maj exp, level, stats | PUT | /players/{id}/exp
maj name | PUT | /players/{id}/name
supprimer un Player | DELETE | /players/{id}

### voir swagger pour + de details
### for all routes, the base url is `http://localhost:8080/api/v1`
