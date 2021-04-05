from exceptions.OperacaoInvalidaError import OperacaoInvalidaError
from ProblemaHeuristico import ProblemaHeuristico
from Estado import Estado

# TODO revisar
# heuristica: sempre optar por aspirar ou ir para salas limpas
class BuscaGulosa:
    def __init__(self, problema: ProblemaHeuristico):
        self.problema = problema
        self.visitados = []
        self.caminho = []

    def resolver(self):
        self.visitados.append(Estado(estado=self.problema.estado_atual))
        while True:
            estado_pai = Estado(estado=self.visitados[-1])
            self.problema.resetar_estado(estado_pai)
            self.caminho.append(Estado(estado=estado_pai))

            if self.problema.sala_atual_suja():
                self.problema.aspirar()
                self.registrar_novo_estado(estado_pai)
                continue

            try:
                if self.problema.sala_direita_suja():
                    self.problema.mover_direira()
                    self.registrar_novo_estado(estado_pai)
                    continue
            except OperacaoInvalidaError:
                pass

            try:
                self.problema.mover_esquerda()
                self.registrar_novo_estado(estado_pai)
            except OperacaoInvalidaError:
                pass

    def registrar_novo_estado(self, pai: Estado):
        self.vericar_se_resolvido()
        self.visitados.append(self.problema.estado_atual)
        self.problema.resetar_estado(pai)

    def vericar_se_resolvido(self):
        if self.problema.resolvido:
            self.caminho.append(self.problema.estado_atual)
            self.mostrar_resultados()
            raise StopIteration

    def mostrar_resultados(self):
        print("Problema resolvido")
        print("Estado final:")
        print(self.problema.estado_atual)
        print("\n")
        for visitado in self.caminho:
            print(visitado)


if __name__ == '__main__':
    problema = ProblemaHeuristico(5, 4)
    busca_cega = BuscaGulosa(problema)
    try:
        busca_cega.resolver()
    except StopIteration:
        print("fim")
