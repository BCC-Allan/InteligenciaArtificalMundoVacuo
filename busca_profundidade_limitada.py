from OperacaoInvalidaError import OperacaoInvalidaError
from EstadoComProfundidade import EstadoComProfundidade
from ProblemaComProfundidade import ProblemaComProfundidade


class BuscaProfundidadeLimitada:
    def __init__(self, problema: ProblemaComProfundidade, limite: int):
        self.problema = problema
        self.visitados = []
        self.caminho = []
        self.pilha = []
        self.limite = limite

    def resolver(self):
        self.pilha.append(EstadoComProfundidade(estado=problema.estado_atual))
        self.visitados.append(EstadoComProfundidade(estado=problema.estado_atual))
        while True:
            self.verificar_problema_impossivel()

            estado_pai = EstadoComProfundidade(estado=self.pilha.pop())

            if estado_pai.nivel_profundidade == self.limite:
                print('\n')
                print(f'Nó de de profundidade {self.limite}')
                print(estado_pai)
                print("Voltando na pilha...\n")
                continue
            self.problema.resetar_estado(estado_pai)
            self.caminho.append(EstadoComProfundidade(estado=estado_pai))

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

    def registrar_novo_estado(self, pai: EstadoComProfundidade):
        self.vericar_se_resolvido()

        if problema.estado_atual not in self.visitados:
            self.pilha.append(problema.estado_atual)
            self.visitados.append(problema.estado_atual)

        self.problema.resetar_estado(pai)

    def vericar_se_resolvido(self):
        if self.problema.resolvido:
            self.caminho.append(self.problema.estado_atual)
            self.mostrar_resultados()

    def mostrar_resultados(self):
        maxima_profundidade = max([estado.nivel_profundidade for estado in self.caminho])
        print("Problema resolvido")
        print(f"Profundidade maxima dos visitados = {maxima_profundidade}")
        print("Estado final:")
        print(self.problema.estado_atual)
        print("\n")
        for visitado in self.caminho:
            print(visitado)
        exit(0)

    def verificar_problema_impossivel(self):
        if not self.pilha:  # pilha vazia
            print(f"Não foi possivel resolver o problema com limite de {self.limite}")
            exit(0)


if __name__ == '__main__':
    problema = ProblemaComProfundidade(5, 2)
    busca_cega = BuscaProfundidadeLimitada(problema, 12)
    busca_cega.resolver()
