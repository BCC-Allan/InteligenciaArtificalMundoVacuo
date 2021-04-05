from Problema import Problema
from EstadoComProfundidade import EstadoComProfundidade


class ProblemaComProfundidade(Problema):
    def __init__(self, numero_salas=3, posicao_aspirador=0):
        super().__init__(numero_salas, posicao_aspirador)
        self.estado_atual = EstadoComProfundidade(0, numero_salas, posicao_aspirador)

    def resetar_estado(self, estado: EstadoComProfundidade):
        self.estado_atual = EstadoComProfundidade(estado=estado)

    def mover_esquerda(self):
        super().mover_esquerda()
        self.estado_atual.incrementar_profundidade()

    def mover_direira(self):
        super().mover_direira()
        self.estado_atual.incrementar_profundidade()

    def aspirar(self):
        super().aspirar()
        self.estado_atual.incrementar_profundidade()
