from OperacaoInvalidaError import OperacaoInvalidaError
from estado import Estado
from problema import Problema


class BuscaLargura:
    def __init__(self, problema: Problema):
        self.problema = problema
        self.visitados = []
        self.fila = []

    def resolver(self):
        self.visitados.append(problema.estado_atual)
        self.fila.append(problema.estado_atual)

        while True:
            estado_pai = Estado(estado=self.fila[0])
            print(estado_pai)

            try:
                self.problema.mover_esquerda()
                self.registrar_novo_estado(estado_pai)
            except OperacaoInvalidaError:
                pass

            try:
                self.problema.mover_direira()
                self.registrar_novo_estado(estado_pai)
            except OperacaoInvalidaError:
                pass

            self.problema.aspirar()
            self.registrar_novo_estado(estado_pai)
            self.fila.pop(0)

    def registrar_novo_estado(self, pai: Estado):
        if self.problema.resolvido:
            print("Problema resolvido!")
            print(self.problema.estado_atual)
            exit(0)

        if problema.estado_atual not in self.visitados:
            self.visitados.append(problema.estado_atual)
            self.fila.append(problema.estado_atual)
        self.problema.resetar_estado(pai)


if __name__ == '__main__':
    problema = Problema(5, 2)
    busca_cega = BuscaLargura(problema)
    busca_cega.resolver()
