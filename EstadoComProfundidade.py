from copy import deepcopy

from Estado import Estado


# 0 = raiz
class EstadoComProfundidade(Estado):
    def __init__(self, nivel_profundidade: int = 0, numero_salas=3, posicao_aspirador=0,
                 estado: 'EstadoComProfundidade' = None):
        if estado:
            self.__dict__.update(deepcopy(estado).__dict__)
            return
        super().__init__(numero_salas, posicao_aspirador)
        self.nivel_profundidade = nivel_profundidade
        self.estado_atual = Estado(numero_salas, posicao_aspirador)

    def incrementar_profundidade(self):
        self.nivel_profundidade += 1

    def __str__(self):
        return super().__str__() + f' | Profundidade = {self.nivel_profundidade}'


