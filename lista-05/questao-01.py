

""" 
Para implementar esta questão, primeiro foi feito a importação da biblioteca random, para poder realizar o sorteio de uma palavra. 

Após isso, temos a definição da lista de palavras. 

Em seguida, é feito o sorteio da palavra, e definido uma lista tentativa[] para armazenar as letras que o usuário acertar. Também é executado um loop for para preencher a lista de tentativa com o caractere "_". 

A variável erro é inicializada em 0, e a mesma tem como função armazenar a quantidade de erros do usuário, assim como servir de variável de controle para o lopp While. 

Desse modo, o loop While se mantém enquanto a quantidade de erros seja menor que 6, mas que também não exista o caractere "_" na lista tentativa[]. 

Dentro do While, o programa executa um input que solicita uma letra ao usuário. 

Após isso, o programa primeiro verifica se a letra pertence a palavra sorteada. Caso seja true, o programa identifica a(s) posição(es) da letra na palavra sorteada, e armazena em um index específico da lista tentativa[]. Caso seja false, o programa notifica o usuário a sua quantidade de erros. 

No fim da estrutura presente dentro do loop While, é exibido o status da tentativa. 

Fora do loop While, o programa verifica a quantidade de erros do usuário, caso seja igual a 6, exibe que o usuário perdeu e exibe a palavra correta. Caso contrário, informa que ele acertou a palavra. 
"""
import random

lista_palavras = ["casa", "bola", "gato", "livro", "mesa", "papel", "janela", "carro", "cachorro", "flor"]

palavra_sorteada = random.choice(lista_palavras)

tentativa = []
tam = len(palavra_sorteada)

for i in range(tam):
    tentativa.append("_")
erro = 0

while erro < 6 and "_" in tentativa:
    
    letra = input("Digite uma letra: ")
    
    if letra in palavra_sorteada:
        for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == letra:
                tentativa[i] = letra
    else:      
        erro += 1
        print(f"Você errou pela {erro}º vez. Tente de novo.")
            
    print(" ".join(tentativa)) 

if erro == 6:
    print("Enforcado")
    print("Palavra Correta: ", palavra_sorteada)
    
else:
    print("Você acertou a palavra!")
    print("Palavra Correta: ", palavra_sorteada)
    
