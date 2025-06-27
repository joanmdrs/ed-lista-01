""" 
Seguindo a lógica de funcionamento do algortimo merge_sort, a lógica de implementação iniciou dividindo a lista em duas partes diferentes, sendo elas: esquerda e direita, onde para cada divisão, o programa realiza uma chamada recursiva para ordenar cada metade.

Quando merge_sort retorna das chamadas recursivas, ela recebe as sublistas já ordenadas, porque cada chamada recursiva já garantiu que as partes menores foram ordenadas. 

A função merge() então apenas junta essas duas listas ordenadas em uma nova lista ordenada.

Para juntar as partes, a função merge() percorre simultaneamente as duas listas (esquerda e direita), comparando os elementos correspondentes. O menor entre os dois é adicionado à lista resultado, e o índice da lista de onde ele veio é incrementado. Esse processo continua até que uma das listas seja completamente percorrida.

Após isso, os elementos restantes da outra lista (que já está ordenada) são adicionados diretamente ao final da lista resultado.

"""

def merge_sort(lista):
    """A recursão continua até as sublistas terem 1 ou 0 elementos:"""
    if len(lista) <= 1:
        return lista 

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
