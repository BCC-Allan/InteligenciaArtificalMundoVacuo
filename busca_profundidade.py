from exceptions.OperacaoInvalidaError import OperacaoInvalidaError
from Estado import Estado
from Problema import Problema


class BuscaProfundidade:
    def __init__(self, problema: Problema):
        self.problema = problema
        self.visitados = []
        self.caminho = []
        self.pilha = []
        self.acc = 0

    def resolver(self):
        self.pilha.append(Estado(estado=problema.estado_atual))
        self.visitados.append(Estado(estado=problema.estado_atual))
        while True:
            self.acc += 1
            estado_pai = Estado(estado=self.pilha.pop())
            self.problema.resetar_estado(estado_pai)
            self.caminho.append(Estado(estado=estado_pai))

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

    def registrar_novo_estado(self, pai: Estado):
        self.vericar_se_resolvido()

        if self.problema.estado_atual not in self.visitados:
            self.pilha.append(self.problema.estado_atual)
            self.visitados.append(self.problema.estado_atual)

        self.problema.resetar_estado(pai)

    def vericar_se_resolvido(self):
        if self.problema.resolvido:
            self.caminho.append(self.problema.estado_atual)
            print(f"Problema resolvido! {self.acc}")
            print(self.problema.estado_atual)
            print("\n")
            for visitado in self.caminho:
                print(visitado)
            raise StopIteration


if __name__ == '__main__':
    problema = Problema(5, 2)
    busca_cega = BuscaProfundidade(problema)
    try:
        busca_cega.resolver()
    except StopIteration:
        print("fim")
