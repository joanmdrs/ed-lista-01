def ordenar_letras(palavra):
    letras = []
    for c in palavra:
        letras.append(c)
    
    # Bubble Sort manual
    n = len(letras)
    for i in range(n):
        for j in range(0, n - i - 1):
            if letras[j] > letras[j + 1]:
                temp = letras[j]
                letras[j] = letras[j + 1]
                letras[j + 1] = temp

    # Montar string ordenada
    chave = ""
    for letra in letras:
        chave += letra
    
    return chave


def agrupar_anagramas(palavras):
    grupos = []       # Lista de grupos de anagramas
    chaves = []       # Lista com as palavras ordenadas para comparar

    for palavra in palavras:
        chave = ordenar_letras(palavra)

        achou = False
        for i in range(len(chaves)):
            if chave == chaves[i]:
                grupos[i].append(palavra)
                achou = True
                break
        
        if not achou:
            chaves.append(chave)
            grupos.append([palavra])
    
    return grupos


# Exemplo de uso
entrada = ["eat", "tea", "tan", "ate", "nat", "bat"]
saida = agrupar_anagramas(entrada)
print(saida)
