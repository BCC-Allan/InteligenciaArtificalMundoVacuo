from exceptions.OperacaoInvalidaError import OperacaoInvalidaError
from ProblemaHeuristico import ProblemaHeuristico
from EstadoComDistancia import EstadoComDistancia


class BuscaAEstrela:
    def __init__(self, problema: ProblemaHeuristico):
        self.problema = problema
        self.visitados = []
        self.caminho = []
        self.estados_a_serem_avaliados = []

    def resolver(self):
        self.visitados.append(EstadoComDistancia(estado=self.problema.estado_atual))
        self.estados_a_serem_avaliados.append(EstadoComDistancia(estado=self.problema.estado_atual))
        while True:
            estado_perto_do_final = min(self.estados_a_serem_avaliados)
            estado_pai = EstadoComDistancia(estado=estado_perto_do_final)
            self.problema.resetar_estado(estado_pai)
            self.estados_a_serem_avaliados = []
            self.caminho.append(EstadoComDistancia(estado=estado_pai))

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

    def registrar_novo_estado(self, pai: EstadoComDistancia):
        self.vericar_se_resolvido()
        self.visitados.append(self.problema.estado_atual)
        self.estados_a_serem_avaliados.append(self.problema.estado_atual)
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
    problema = ProblemaHeuristico(5, 2)
    busca_cega = BuscaAEstrela(problema)
    try:
        busca_cega.resolver()
    except StopIteration:
        print("fim")
