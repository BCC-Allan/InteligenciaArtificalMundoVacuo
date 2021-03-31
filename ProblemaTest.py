from busca_cega import BuscaCega
from largura_model1 import LarguraModel1
from problema import Problema


def teste_aleatorio():
    numero_salas = 3
    for posicao_aspirador in range(numero_salas):
        print(posicao_aspirador)
        problema = Problema(3, posicao_aspirador)
        busca_cega = BuscaCega(problema)
        busca_cega.resolver()
        assert busca_cega.problema.resolvido, \
            f'O problema com o aspirador na posicao {posicao_aspirador} deu ruim \n' \
            f'{problema.estado_atual}'

    print("Teste passou")


def teste():
    numero_salas = 5
    for posicao_aspirador in range(numero_salas):
        print(posicao_aspirador)
        problema = Problema(3, posicao_aspirador)
        largura = LarguraModel1(problema)
        largura.resolver()
        assert largura.problema.resolvido, \
            f'O problema com o aspirador na posicao {posicao_aspirador} deu ruim \n' \
            f'{problema.estado_atual}'

    print("Teste passou")


if __name__ == '__main__':
    teste()
