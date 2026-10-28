from personagem import Personagem 
from utils import falar


class Heroi(Personagem):
    
    def __init__(self, nome, vida, ataque, defesa, pocoes=2, falas=None):
        super().__init__(nome, vida, ataque, defesa, falas)
        self.pocoes = pocoes

    def usar_pocao(self):
        if self.pocoes > 0:
            self.pocoes -= 1
            curado = self.curar(15) 
            falar(f'{self.nome} bebeu uma poção de recuperação e recuperou {curado} de vida 'f"poçoes restantes: self.pocoes")
            return True
        falar(f"{self.nome} acabou as poções (T-T)")
        return False


    def atacar(self, personagem):
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.receber_dano(self.ataque)


    def salvar_refem(self, vilao):
        falar(f"{self.nome} abre a sela e liberta o Caesar Zepelli")
        falar(f"Caesar: Obrigado, {self.nome}. o {vilao.nome} me prendeu por dias")
        falar(f"Ele falava sobre a volta dos Pilares para o fim de PAI-THON")
        falar(f"Os pilares buscam a pedra de rubi para realizar seus planos")
        falar(f"{self.nome}, irei te ajudar a impedir o retorno dos pilares" )
    

    def __str__(self):
        return f"Herói: {super().__str__()} | Poções: {self.pocoes}"