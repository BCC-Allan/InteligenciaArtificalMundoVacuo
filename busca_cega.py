from problema import Problema


class BuscaCega:
    def __init__(self, problema: Problema):
        self.problema = problema

    def resolver(self):
        # true == esquerda false == direira
        flag_direcao = True
        acc = 0
        while not self.problema.resolvido:
            acc += 1
            self.problema.aspirar()
            try:
                if flag_direcao:
                    self.problema.mover_direira()
                    continue
                self.problema.mover_esquerda()
            except ValueError:
                flag_direcao = not flag_direcao
                continue

        self.final(add=f"Rodadas: {acc}")

    def final(self, add=''):
        print(f"\nPROBLEMA FINALIZADO | {add}")
        print(self.problema.estado_atual)


if __name__ == '__main__':
    problema = Problema(5, 1)
    busca_cega = BuscaCega(problema)
    busca_cega.resolver()
