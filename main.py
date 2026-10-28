import random
from heroi import Heroi
from vilao import Vilao
from utils import (falar, titulo, barra, ler_numero, sortear_pergunta,fazer_pergunta, mostrar_historico)

HEROI = [
    {"nome": "Pyone", "vida": 44, "ataque": 10, "defesa": 2, "pocoes": 2, "falas": {
        "desafio": ["você não passara javier", "O reino de PAI-THON não caira"],
        "vitoria": ["Pyone aquele que nunca morre", "Javier foi compilado pelo reino de PAI-THON"],
    }},
]

VILOES = [
    {"nome": "Javier", "vida": 30, "ataque": 10, "defesa": 2, "falas": {
        "desafio": ["O lord Javier acabara com o reino de PAI-THON", "Javier o lord no comando"],
        "abalado": ["Javier não desiste tão facil", "eu não posso ser derrotado"],
        "derrota": ["Eu não aceito sua piedade", "Outros virão depois de mim"],
    }},
]


def escolher_heroi():
    titulo("ESCOLHA SEU HERÓI")
    for i, dados in enumerate(HEROI, start=1):
        print(f"{i}. {dados['nome']} | Vida {dados['vida']} | Ataque {dados['ataque']} | "
              f"Defesa {dados['defesa']} | Poções {dados['pocoes']}")
    escolha = ler_numero("Herói: ", 1, len(HEROI))
    return Heroi(**HEROI[escolha - 1])


def mostrar_status(heroi, vilao):
    print()
    for p in (heroi, vilao):
        print(f"{p.nome:<8} {barra(p.vida, p.vida_maxima)} {p.vida}/{p.vida_maxima}")
    print(f"Poções: {heroi.pocoes}")


def batalha(heroi, vilao):
    
    titulo(f"{heroi.nome} VS {vilao.nome}")
    vilao.dialogar(heroi, "desafio")

    while heroi.esta_vivo() and vilao.esta_vivo():
        mostrar_status(heroi, vilao)
        print("\n1. Atacar (responder o quiz)")
        print("2. Usar poção")
        print("3. Dialogar")
        print("4. Ver histórico")
        escolha = ler_numero("O que você quer fazer? ", 1, 4)

        vilao_age = True

        if escolha == 1:
            if fazer_pergunta(sortear_pergunta()):
                heroi.atacar(vilao)
            else:
                falar(f"{heroi.nome} errou a resposta e o ataque falhou!")
        elif escolha == 2:
            if not heroi.usar_pocao():
                continue   
        elif escolha == 3:
            heroi.dialogar(vilao, "desafio")
            if random.random() < 0.30:
                vilao.dialogar(heroi, "abalado")
                falar(f"{vilao.nome} ficou abalado e perdeu a vez!")
                vilao_age = False
            else:
                vilao.dialogar(heroi, "desafio")
        elif escolha == 4:
            mostrar_historico()
            continue

        if vilao.esta_vivo() and vilao_age:
            vilao.atacar(heroi)

    return heroi.esta_vivo()


def main():
    titulo("QUIZ HEROES")
    heroi = escolher_heroi()

    for numero, dados in enumerate(VILOES, start=1):
        titulo(f"FASE {numero} de {len(VILOES)}")
        vilao = Vilao(**dados)

        if not batalha(heroi, vilao):
            titulo("DERROTA")
            falar(f"{heroi.nome} caiu na fase {numero}... Tente de novo!")
            break

        vilao.dialogar(heroi, "derrota")
        heroi.dialogar(vilao, "vitoria")
        falar(f"{vilao.nome} foi derrotado!")
        heroi.salvar_refem(vilao)
    else:
        titulo("VITÓRIA!")
        falar(f"{heroi.nome} derrotou todos os vilões e salvou o reino!")

    mostrar_historico()


if __name__ == "__main__":
    main()