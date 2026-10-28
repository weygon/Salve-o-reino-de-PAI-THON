import random

PERGUNTAS = [
    {"texto": "Qual função mostra texto na tela?", "opcoes": ["print()", "echo()", "write()"], "resposta": 1},
    {"texto": "Qual é o operador de multiplicação em Python?", "opcoes": ["+", "=", "*"], "resposta": 3},
    {"texto": "Qual função converte um número em texto (string)?", "opcoes": ["int()", "str()", "float()"], "resposta": 2},
    {"texto": "Qual tipo de dado que guarda True ou False?", "opcoes": ["str", "int", "bool"], "resposta": 3},
    {"texto": "Qual palavra cria uma função em Python?", "opcoes": ["def", "func", "make"], "resposta": 1},
    {"texto": "Qual é o simbolo para declarar variavel em python?", "opcoes": ["==","=", "!="], "resposta": 2},
    {"texto": "bola = redonda, o que o print(bola) vai mostrar?", "opcoes": ["quadrada","bola", "redonda"], "resposta":3},
    {"texto": "nota = 9.5, qual é o tipo de dado da a variavel nota?", "opcoes": ["int", "str", "float"], "resposta": 3},
]

_fila_perguntas = []

HISTORICO = []

def falar(texto):
    print(texto)
    HISTORICO.append(texto)

def mostrar_historico():
    titulo("Historico de ações")
    if not HISTORICO:
        print("não aconteceu nada ainda..., jogue um pouco antes")
    for numero, acao in enumerate(HISTORICO, start=1):
        print(f"{numero:02d}. {acao}")
    print("=" * 44)


def titulo(texto):
    print("=" * 44)
    print(f"{texto:^44}")
    print("=" * 44)


def barra(vida, vida_maxima, tamanho=19):
    cheio = round(tamanho*vida/vida_maxima)
    return "[" + '#' * cheio + '-' * (tamanho - cheio) + "]"


def ler_numero(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))
            if minimo <= numero <= maximo:
                return numero
        except ValueError:
            pass
        print(f"escolha de {minimo} a {maximo}.")


def sortear_pergunta():
    if not _fila_perguntas:
        _fila_perguntas.extend(PERGUNTAS)
        random.shuffle(_fila_perguntas)
    return _fila_perguntas.pop()



def fazer_pergunta(pergunta):
    print("\n" + pergunta["texto"])
    for i, opcao in enumerate(pergunta["opcoes"], start=1):
        print(f"{i}. {opcao}")

    reposta = ler_numero("Escolha uma opção: ", 1, len(pergunta["opcoes"]))

    if reposta == pergunta["resposta"]:
        falar("Resposta correta, bate nele (⌒ ‿ ⌒)")
        return True
    falar("resposta errada (T-T)")
    return False
