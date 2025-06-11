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
