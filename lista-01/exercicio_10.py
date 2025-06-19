"""
Para este exercício, foram definidas duas funções principais: `ordenar_letras` e `agrupar_anagramas`.

O objetivo geral do programa é agrupar palavras que sejam anagramas, ou seja, que possuem as mesmas letras, mas em ordens diferentes.
"""

"""
A função ordenar_letras recebe como parâmetro uma palavra (string) e retorna essa palavra com suas letras ordenadas em ordem alfabética.

Essa ordenação serve para gerar uma 'chave' que identifique grupos de anagramas. Palavras com a mesma chave são anagramas.

Para ordenar as letras, foi utilizado o algoritmo Bubble Sort, que compara pares de letras adjacentes e os troca de posição se estiverem fora de ordem.
"""

def ordenar_letras(palavra):
    letras = []
    for c in palavra:
        letras.append(c)
    
    n = len(letras)
    for i in range(n):
        for j in range(0, n - i - 1):
            if letras[j] > letras[j + 1]:
                temp = letras[j]
                letras[j] = letras[j + 1]
                letras[j + 1] = temp

    chave = ""
    for letra in letras:
        chave += letra
    
    return chave

"""
A função agrupar_anagramas, por usa vez, recebe como parâmetro uma lista de palavras.

Seu objetivo é agrupar essas palavras em sublistas, onde cada sublista contém palavras que são anagramas entre si.

Para isso, a função inicializa duas listas auxiliares. 
- grupos: responsável por armazenar os grupos de anagramas.
- chaves: responsável por armazenar as versões ordenadas das palavras, para fins de comparação.

Sendo assim, a lógica segue a seguinte sequência:
1. Ordenar a palavra (usando a função ordenar_letras).
2. Verificar se a chave já foi encontrada antes.
3. Se sim, adicionar a palavra ao grupo correspondente.
4. Se não, criar um novo grupo com essa palavra e registrar a nova chave.
"""
def agrupar_anagramas(palavras):
    """ Lista onde cada elemento será um frupo de anagramas."""
    grupos = []  
    """ Lista onde serão guardadas as chaves, ou seja, as palavras ordenadas. """
    chaves = [] 

    """Executa um loop for que percorre a lista de palavras"""
    for palavra in palavras:
        
        """Obtém a chave da palavra"""
        chave = ordenar_letras(palavra)

        """Variável de controle que indica se a chave já foi encontrada"""
        achou = False 
        
        """Esse for percorre todas as chaves já registradas."""
        for i in range(len(chaves)):
            """Aqui o programa verifica se a chave da palavra atual já está na lista chaves."""
            if chave == chaves[i]:
                """Se a chave já existe, adiciona a palavra ao grupo correspondente"""
                grupos[i].append(palavra)
                achou = True
                break
        
        """Se a chave ainda não foi encontrada, cria novo grupo e registra a chave"""
        if not achou:
            chaves.append(chave)
            grupos.append([palavra])
    
    """Retorna todos os grupos encontrados"""
    return grupos

entrada = ["eat", "tea", "tan", "ate", "nat", "bat"]
saida = agrupar_anagramas(entrada)
print(saida)
