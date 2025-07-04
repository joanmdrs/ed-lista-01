#Questão 1:

"""Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de uma lista e escolherá uma palavra aleatoriamente. O jogador vai tentar descobrir essa palavra, mas só poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

Quando errar pela 6ª vez imprimir: Enforcado e exibir a palavra correta
"""
import random

lista_palavras = ["casa", "bola", "gato", "livro", "mesa", "papel", "janela", "carro", "cachorro", "flor"]

palavra_sorteada = random.choice(lista_palavras)

tam = len(palavra_sorteada)
tentativa = []

for i in range(tam):
    tentativa.append("_")
erro = 0

print("Palavra sorteada: ", palavra_sorteada)
while erro < 6 and "_" in tentativa:
    
    letra = input("Digite uma letra: ")
    
    if letra.lower() not in palavra_sorteada:
        erro += 1
        print(f"Você errou pela {erro}º vez. Tente de novo.")
    
    if letra in palavra_sorteada:
        for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == letra:
                tentativa[i] = letra
            
    print(" ".join(tentativa)) 

if erro == 6:
    print("Enforcado")
    print("Palavra Correta: ", palavra_sorteada)
    
else:
    print("Você acertou a palavra!")
    print("Palavra Correta: ", palavra_sorteada)
    
