from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Golduck(Poison):
    def __init__(self):
        moves = [
            Move("Crunch", "", 40),
            Move("Poison Jab", "", 40),
            Move("Bite", "", 80),
            Move("Mud Bomb", "", 0)
        ]
        super().__init__("Grimer", 80, moves, "./TVPoke/Pokemon/imgs/Grimer.png")