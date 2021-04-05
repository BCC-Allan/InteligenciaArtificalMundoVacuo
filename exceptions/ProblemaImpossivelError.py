class ProblemaImpossivelError(Exception):

    def __init__(self, causa: str):
        super().__init__(f'O problema não possui solução com o algoritimo atual pois: {causa}')
