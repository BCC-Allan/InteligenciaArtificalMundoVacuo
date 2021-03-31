from typing import Dict, List

from problema import Problema


class LarguraModel1:

    def __init__(self, problema: Problema):
        self.problema = problema

    def resolver(self):
        # true == esquerda false == direira
        flag_direcao = True
        acc = 0
        while not self.problema.resolvido:
            acc += 1
            try:
                if not self.problema.aspirado():
                    self.anda_na_direcao(flag_direcao)
                    continue
                self.problema.aspirar()
                if self.problema.resolvido: # somente para o print
                    continue
                flag_direcao = not flag_direcao
                self.anda_na_direcao(flag_direcao)
            except ValueError:
                flag_direcao = not flag_direcao
                self.anda_na_direcao(flag_direcao)
                continue

        self.final(add=f'Rodadas: {acc}')

    def anda_na_direcao(self, flag_direcao):

        if self.problema.direita_visto():
            self.problema.mover_esquerda()
            return

        if self.problema.esquerda_visto():
            self.problema.mover_direira()
            return

        if flag_direcao:
            self.problema.mover_direira()
        else:
            self.problema.mover_esquerda()

    def final(self, add=''):
        print(f"\nPROBLEMA FINALIZADO | {add}")
        print(self.problema.estado_atual)


if __name__ == '__main__':
    problema = Problema(5, 4)
    larguraModel1 = LarguraModel1(problema)
    larguraModel1.resolver()
