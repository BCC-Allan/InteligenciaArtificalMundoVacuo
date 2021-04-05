"""
 Classe que representa o estado
"""
from copy import deepcopy


class Estado:
    def __init__(self, numero_salas=3, posicao_aspirador=0, estado: 'Estado' = None):
        """
        Salas = [False, False, False]
        cada index do array é uma sala, sendo 0 para limpo 1 para sujo
        """

        if estado:
            self.__dict__.update(deepcopy(estado).__dict__)
            return

        self.numero_salas = numero_salas
        self.salas = [True for i in range(self.numero_salas)]
        self.posicao_aspirador = posicao_aspirador

    def incrementar_posicao(self):
        self.posicao_aspirador += 1

    def decrementar_posicao(self):
        self.posicao_aspirador -= 1

    def trocar_estado(self):
        self.salas[self.posicao_aspirador] = False

    # Retorna true se todos os elementos são falsos
    @property
    def teste_objetivo(self):
        return not any(self.salas)

    def __str__(self):
        salas = [
            f'[X] {str(self.salas[i]).rjust(5, " ")}'
            if self.posicao_aspirador == i
            else f'[ ] {str(self.salas[i]).rjust(5, " ")}'
            for i in range(self.numero_salas)
        ]

        return ' | '.join(salas)

    def __eq__(self, other):
        return self.salas == other.salas and self.posicao_aspirador == other.posicao_aspirador
