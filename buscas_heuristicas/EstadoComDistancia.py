from copy import deepcopy
from Estado import Estado
from functools import reduce


class EstadoComDistancia(Estado):
    SALA_LIMPA = False
    SALA_SUJA = True

    def __init__(self, numero_salas=3, posicao_aspirador=0, estado: 'EstadoComDistancia' = None):
        if estado:
            self.__dict__.update(deepcopy(estado).__dict__)
            return

        super().__init__(numero_salas, posicao_aspirador)

    @property
    def sala_atual(self) -> bool:
        return self.salas[self.posicao_aspirador]

    @property
    def distancia(self):
        if self.teste_objetivo:
            return 0
        qtd_salas_sujas = reduce(lambda a, b: a + b, self.salas)
        # esta mais perto da solução se ja estiver em uma sala suja

        adicional_estar_sala_suja = 0 if self.sala_atual == self.SALA_SUJA else 1
        return qtd_salas_sujas + adicional_estar_sala_suja

    def __lt__(self, other):
        return self.distancia < other.distancia

    def __eq__(self, other):
        return self.distancia == other.distancia

    def __gt__(self, other):
        return self.distancia > other.distancia

    def __str__(self):
        return super().__str__() + f' | Distancia = {self.distancia}'
