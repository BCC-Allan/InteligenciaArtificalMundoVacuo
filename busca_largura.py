from OperacaoInvalidaError import OperacaoInvalidaError
from Estado import Estado
from Problema import Problema


class BuscaLargura:
    def __init__(self, problema: Problema):
        self.problema = problema
        self.visitados = []
        self.fila = []
        self.acc = 0

    def resolver(self):
        self.visitados.append(problema.estado_atual)
        self.fila.append(problema.estado_atual)
        while True:
            self.acc += 1
            estado_pai = Estado(estado=self.fila[0])
            self.problema.resetar_estado(Estado(estado=self.fila[0]))
            # print(f"Estado pai:\n{estado_pai}")

            try:
                self.problema.mover_esquerda()
                # print(f"Movendo para a esquerda: {self.problema.estado_atual}")
                self.registrar_novo_estado(estado_pai)
            except OperacaoInvalidaError:
                pass

            try:
                self.problema.mover_direira()
                # print(f"Movendo para a direita: {self.problema.estado_atual}")
                self.registrar_novo_estado(estado_pai)
            except OperacaoInvalidaError:
                pass

            self.problema.aspirar()
            # print(f"Aspirando: {self.problema.estado_atual}")
            self.registrar_novo_estado(estado_pai)
            # print("fim dos filhos\n")
            self.fila.pop(0)

    def registrar_novo_estado(self, pai: Estado):
        if self.problema.resolvido:
            # print(f"Problema resolvido! {self.acc}")
            print(self.problema.estado_atual)
            print("\n")
            for visitado in self.visitados:
                print(visitado)
            exit(0)

        if problema.estado_atual not in self.visitados:
            # print("novo estado na fila")
            self.visitados.append(problema.estado_atual)
            self.fila.append(problema.estado_atual)
        self.problema.resetar_estado(pai)


if __name__ == '__main__':
    problema = Problema(3, 1)
    busca_cega = BuscaLargura(problema)
    busca_cega.resolver()
