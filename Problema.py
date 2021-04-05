# Estados
# Operadores
# Teste objetivo
# custo do caminho
from Estado import Estado
from exceptions.OperacaoInvalidaError import OperacaoInvalidaError


class Problema:
    def __init__(self, numero_salas=3, posicao_aspirador=0):
        self.estado_atual = Estado(numero_salas, posicao_aspirador)

    # operadores
    def mover_esquerda(self):
        if self.estado_atual.posicao_aspirador == 0:
            raise OperacaoInvalidaError('ir para a esquerda')
        self.estado_atual.decrementar_posicao()

    def mover_direira(self):
        if self.estado_atual.posicao_aspirador == self.estado_atual.numero_salas - 1:
            raise OperacaoInvalidaError('ir para a esquerda')
        self.estado_atual.incrementar_posicao()

    def aspirar(self):
        self.estado_atual.trocar_estado()

    @property
    def resolvido(self):
        return self.estado_atual.teste_objetivo

    def resetar_estado(self, estado: Estado):
        self.estado_atual = Estado(estado=estado)
