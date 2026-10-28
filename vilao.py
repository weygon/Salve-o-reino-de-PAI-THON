from personagem import Personagem 
import random
from utils import falar


class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa, falas=None):
        super().__init__(nome, vida, ataque, defesa, falas)

    def atacar(self, alvo):
        dano = self.ataque
        if random.random() < 0.25:
            falar(f"{self.nome} usa Boilerplate Code contra {alvo.nome}")
            dano = int(self.ataque * 1.5)
        else:
            falar(f"{self.nome} ataca {alvo.nome}")
        alvo.receber_dano(dano)


    def __str__(self):
        return f"Vilão: {super().__str__()}"