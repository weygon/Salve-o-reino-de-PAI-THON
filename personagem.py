import random
from utils import falar

class Personagem:

    
    def __init__(self, nome, vida, ataque, defesa, falas=None):
        self.nome = nome
        self.ataque = ataque
        self.vida = vida
        self.vida_maxima = vida
        self.defesa = defesa
        self.falas = falas or {}


    def receber_dano(self, dano):
        
        dano_real = max(0, dano - self.defesa)
        self.vida = max(0, self.vida - dano_real)
        falar(f'{self.nome} recebeu {dano_real} de dano! Vida atual: {self.vida}')


    def esta_vivo(self):
        return self.vida > 0


    def curar(self, quantidade):
       
        antes = self.vida
        self.vida = min(self.vida_maxima, self.vida + quantidade)
        return self.vida - antes


    def dialogar(self, outro, situacao="desafio"):
        fala = random.choice(self. falas[situacao])
        falar(f'{self.nome} diz para {outro.nome}: "{fala}"')


    def status(self):
        return{
            "nome":self.nome,
            "vida":self.vida,
            "ataque":self.ataque,
            "defesa":self.defesa,
        }

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado


    def definir_defesa(self, defesa):
        """
        Aumenta a defesa do personagem.
        """
        self.defesa += defesa
        print(f'Defesa de {self.nome} aumentada para: {self.defesa}')


    def __str__(self):
        return f'Personagem: {self.nome} |vida: {self.vida}/{self.vida_maxima} | ataque: {self.ataque} | Defesa: {self.defesa}'
