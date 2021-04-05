class OperacaoInvalidaError(Exception):

    def __init__(self, operacao: str):
        super().__init__(f'A operação de {operacao} é invalida no atual contexto')
