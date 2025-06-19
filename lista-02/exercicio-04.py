class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        return self.pilha.pop()
    
    def size(self):
        return len(self.pilha)
    
    def elementos(self):
        return self.pilha[:]


def verifica_pilhas_iguais(pilha_1, pilha_2):
    print("\n>>> VERIFICA PILHAS IGUAIS <<<")

    if pilha_1.elementos() == pilha_2.elementos():
        return "As pilhas são iguais."
    elif pilha_1.size() > pilha_2.size():
        return "As pilhas são diferentes. A pilha 01 é maior."
    elif pilha_2.size() > pilha_1.size():
        return "As pilhas são diferentes. A pilha 02 é maior."
    else:
        return "As pilhas têm o mesmo tamanho, mas elementos diferentes."


def verifica_estatisticas_pilha(pilha):
    elementos = pilha.elementos()
    if not elementos:
        print("A pilha está vazia.")
        return

    maior = elementos[0]
    menor = elementos[0]
    soma = 0

    for i in elementos:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        soma += i

    media = soma / pilha.size()

    print("\n>>> ESTATÍSTICAS DA PILHA <<<")
    print("Maior elemento da pilha:", maior)
    print("Menor elemento da pilha:", menor)
    print("Média dos elementos da pilha:", media)


def transferir_elementos(pilha_1, pilha_2):
    for i in pilha_1.elementos():
        pilha_2.push(i)

    print("\n>>> TRANSFERÊNCIA DE ELEMENTOS <<<")
    print("Pilha Original:", pilha_1.elementos())
    print("Cópia da Pilha:", pilha_2.elementos())


def contar_elementos_impares(pilha):
    cont_impares = 0
    for i in pilha.elementos():
        if i % 2 != 0:
            cont_impares += 1
    print("\n>>> ELEMENTOS ÍMPARES <<<")
    print("A pilha fornecida contém:", cont_impares, "elementos ímpares")


def contar_elementos_pares(pilha):
    cont_pares = 0
    for i in pilha.elementos():
        if i % 2 == 0:
            cont_pares += 1
    print("\n>>> ELEMENTOS PARES <<<")
    print("A pilha fornecida contém:", cont_pares, "elementos pares")


pilha1 = Pilha()
pilha2 = Pilha()

for i in range(1,10):  
    pilha1.push(i)

for j in range(1,5):   
    pilha2.push(j)

# 1. VERIFICA PILHA IGUAIS
print(verifica_pilhas_iguais(pilha1, pilha2))

# 2. VERIFICA ESTATÍSTICAS DE CADA PILHA
verifica_estatisticas_pilha(pilha1)
verifica_estatisticas_pilha(pilha2)

# 3. TRANSFERE OS ELEMENTOS DE UMA PILHA PARA OUTRA
transferir_elementos(pilha1, pilha2)

# 4. CONTA QUANTOS ELEMENTOS DA PILHA SÃO ÍMPARES
contar_elementos_impares(pilha1)

# 5. CONTA QUANTOS ELEMENTOS DA PILHA SÃO PARES
contar_elementos_pares(pilha1)
