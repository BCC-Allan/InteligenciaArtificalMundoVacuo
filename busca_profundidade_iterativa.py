from ProblemaComProfundidade import ProblemaComProfundidade
from busca_profundidade_limitada import BuscaProfundidadeLimitada
from exceptions.ProblemaImpossivelError import ProblemaImpossivelError

if __name__ == '__main__':
    problema = ProblemaComProfundidade(6, 1)
    limite_do_limite = 100
    generator = (BuscaProfundidadeLimitada(problema, limite=limite) for limite in range(limite_do_limite + 1))
    for busca_limitada in generator:
        try:
            busca_limitada.resolver()
        except ProblemaImpossivelError:
            continue
        except StopIteration:
            print(f"Problema resolvido com no minimo {busca_limitada.limite}!!!!!!!!")
            break
