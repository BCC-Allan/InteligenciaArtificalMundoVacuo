# Estados
# Operadores
# Teste objetivo
# custo do caminho
from estado import Estado


class Problema:
    def __init__(self, numero_salas, posicao_aspirador):
        self.estado_atual = Estado(numero_salas, posicao_aspirador)

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
        print(f'---- {self.estado_atual} ----')

    @property
    def posicao_atual(self):
        return self.estado_atual.posicao_aspirador

    @property
    def resolvido(self):
        return self.estado_atual.teste_objetivo

    def pode_direita(self):
        return self.estado_atual.posicao_aspirador == self.estado_atual.numero_salas - 1

    def pode_esquerda(self):
        return self.estado_atual.posicao_aspirador == 0

    def aspirado(self):
        return self.estado_atual.salas[self.posicao_atual]

    def esquerda_visto(self):
        return not self.estado_atual.salas[0]

    def direita_visto(self):
        return not self.estado_atual.salas[-1]
