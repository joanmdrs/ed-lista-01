""" 
Para implementar este exercício, foi criado uma função que recebe como parâmetro da lista a ser ordenada.

Dentro da função, fazemos a leitura do tamanho da lista e guardamos em N.

Em seguida uma estrura de loop for que percorre a lista a partir do índice 1, partindo do princípio que o primeiro elemento (posição 0) já é considerado parte da lista ordenada. 

Após isso, como dito no enunciado do exercício, pegamso um elemento da lista, e definimos j = i - 1, para comparar esse item com os elementos anteriores da parte ordenada.

Sendo assim, criamos uma estrutura de while, cuja condição é que : enquanto o valor de j for maior ou igual a zero e o elemento da posição j for maior que o item, os elementos são deslocados uma posição à frente, abrindo espaço para inserção.

Por fim, quando a posição correta é encontrada, o item é inserido nessa posição, e o processo se repete para o próximo elemento da lista.

Dessa forma, a cada iteração do loop externo, a parte inicial da lista vai se tornando ordenada, até que toda a lista esteja ordenada.

"""

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        item = lista[i]
        j = i - 1
         
        while j >= 0 and lista[j] > item:
            lista[j + 1] = lista[j]
            j = j - 1;    
            
        lista[j + 1] = item
    return lista
        
lista = [50, 12, 5, 69, 1, 56, 10, 2]
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)