# Estados
# Operadores
# Teste objetivo
# custo do caminho
from estado import Estado
from copy import deepcopy


class Problema:
    def __init__(self, numero_salas=3, posicao_aspirador=0, novo_estado: Estado = None):
        self.estado_atual = Estado(numero_salas, posicao_aspirador) or deepcopy(novo_estado)

    # operadores

    def mover_esquerda(self):
        if self.estado_atual.posicao_aspirador == 0:
            raise ValueError('O aspirador não pode ir para a esquerda')
        self.estado_atual.decrementar_posicao()

    def mover_direira(self):
        if self.estado_atual.posicao_aspirador == self.estado_atual.numero_salas - 1:
            raise ValueError('O aspirador não pode ir para a direita')
        self.estado_atual.icrementar_posicao()

    def aspirar(self):
        self.estado_atual.trocar_estado()

    @property
    def resolvido(self):
        return self.estado_atual.teste_objetivo

    def resetar_estado(self, estado: Estado):
        self.estado_atual = deepcopy(estado)

    def get_estado_atual(self):
        return deepcopy(self.estado_atual)
