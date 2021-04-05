from Problema import Problema
from exceptions.OperacaoInvalidaError import OperacaoInvalidaError
from functools import reduce

class ProblemaHeuristico(Problema):
    SALA_LIMPA = False
    SALA_SUJA = True

    @property
    def sala_atual(self) -> bool:
        return self.estado_atual.salas[self.estado_atual.posicao_aspirador]

    def sala_atual_limpa(self) -> bool:
        return self.sala_atual == self.SALA_LIMPA

    def sala_atual_suja(self) -> bool:
        return self.sala_atual == self.SALA_SUJA

    def sala_direita_suja(self) -> bool:
        try:
            return self.estado_atual.salas[self.estado_atual.posicao_aspirador + 1] == self.SALA_SUJA
        except IndexError:
            raise OperacaoInvalidaError('Verificar a sala da direita')

    def sala_esquerda_suja(self) -> bool:
        try:
            return self.estado_atual.salas[self.estado_atual.posicao_aspirador - 1] == self.SALA_SUJA
        except IndexError:
            raise OperacaoInvalidaError('Verificar a sala da esquerda')
