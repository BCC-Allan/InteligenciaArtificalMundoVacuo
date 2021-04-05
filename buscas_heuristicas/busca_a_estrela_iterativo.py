from exceptions.OperacaoInvalidaError import OperacaoInvalidaError
from ProblemaHeuristico import ProblemaHeuristico
from EstadoComDistancia import EstadoComDistancia


class BuscaAEstrelaIterativo:
    """
        Busca a* com profundiade setada como a menor possivel
    """
    def __init__(self, problema: ProblemaHeuristico, limite: int):
        self.problema = problema
        self.visitados = []
        self.caminho = []
        self.estados_a_serem_avaliados = []
        self.limite = limite
        self.acc = 0

    def resolver(self):
        self.visitados.append(EstadoComDistancia(estado=self.problema.estado_atual))
        self.estados_a_serem_avaliados.append(EstadoComDistancia(estado=self.problema.estado_atual))
        while True:
            self.acc += 1
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
        if self.acc >= self.limite:
            print(f"Não foi possivel resolver com o limite de {self.limite}")
            raise StopIteration

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
        print(f"Deu certo com o limite de {self.limite}")


if __name__ == '__main__':
    for limite in range(1, 13):
        try:
            problema = ProblemaHeuristico(5, 2)
            busca_cega = BuscaAEstrelaIterativo(problema, limite)
            busca_cega.resolver()
        except StopIteration:
            continue
