from busca_cega import BuscaCega
from Problema import Problema


def teste():
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


if __name__ == '__main__':
    teste()
