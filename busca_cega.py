from Problema import Problema


class BuscaCega:
    def __init__(self, problema: Problema):
        self.problema = problema

    def resolver(self):
        # true == esquerda false == direira
        flag_direcao = True
        while not self.problema.resolvido:
            self.problema.aspirar()
            try:
                if flag_direcao:
                    self.problema.mover_direira()
                    continue
                self.problema.mover_esquerda()
            except ValueError:
                flag_direcao = not flag_direcao
                continue
        print("\nPROBLEMA FINALIZADO")
        print(self.problema.estado_atual)


if __name__ == '__main__':
    problema = Problema(3, 1)
    busca_cega = BuscaCega(problema)
    busca_cega.resolver()
