""" 
Para implementar este exercício, foi utilizado a estrutura de lista. Esta estrutura foi escolhida, devido não se saber previamente quantas sugestões o usuário irá fornecer, logo, a estrutura de lista se torna uma boa escolha devido o seu armazenamento dinâmico e flexível.
"""

""" 
A função contar_palavras recebe por parâmetro uma string de caracteres e tem como finalidade realizar a contagem de palavras que a string fornecida contém. 

Primeiro, é definido a variável guarda_palavra acumula caracteres até que seja encontrado um espaço em branco. Desse modo, sempre que um espaço em branco é encontrado, se entende que uma palavra foi formada e a mesma é adiciona à lista de palavras. 

Após o fim da iteração, se houver caracteres armazenados na variável guarda_palavra,a mesma é adicionada a lista de palavras como sendo a última palavra. 

No final da execução, a função contar_palavras retorna a quantidade de elementos da lista de palavras. 

"""

def contar_palavras(mensagem):
    palavras = []
    guarda_palavra = ''
    
    for caractere in mensagem:
        if caractere == ' ':
            if guarda_palavra != '':
                palavras.append(guarda_palavra)
                guarda_palavra = ''
        else:
            guarda_palavra += caractere
    
    if guarda_palavra != '':
        palavras.append(guarda_palavra)

    return len(palavras)


""" 
A função caixa_de_sugestoes contém o código da parte principal desse exercício. 

Esta função implementa a estrutura de repetição While, a qual estabelece que enquanto for verdade, o usuário posso digitar sugestões. No caso do usuário digitar a palavra 'sair', o while é encerrado. 

A variável mensagem armazena a sugestão informada pelo usuário. 

Primeiro, é obtido o tamanho da string, a qual é armazenada na variável tamanho. 

Segundo, a string é passada como parâmetro para a função contar_palavras que retorna a quantidade de palavras presentes na string e armazena essa informação dentro da variável num_palavras.

Terceiro, é executado um condicional que verifica se a sugestão contém mais de 3 palavras e menos de 100 caracteres. Caso sim, a mesma é armazenada na lista de sugestões. 

Ao fim da execução do while, é executado um loop for que percorre a lista de sugestões e as exibe. 
"""

def caixa_de_sugestoes():
    sugestoes = []

    while True:
        mensagem = input("Digite sua sugestão (ou 'sair' para encerrar): ")
        
        if mensagem.lower() == 'sair':
            break
        
        tamanho = len(mensagem)
        num_palavras = contar_palavras(mensagem)

        if num_palavras > 3 and tamanho < 100:
            sugestoes.append(mensagem)
            print("Sugestão armazenada com sucesso!\n")
        else:
            print("Sugestão inválida. Deve ter mais de 3 palavras e menos de 100 caracteres.\n")

    print("\nSUGESTÕES ARMAZENADAS:")
    
    for s in sugestoes:
        print(s)

caixa_de_sugestoes()
