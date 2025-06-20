class Fila:
    def __init__(self):
        self.fila = []

    def queue(self, item):
        self.fila.append(item)  

    def dequeue(self):
        if not self.isEmpty():
            return self.fila.pop(0)
        print("Erro: fila vazia")
        
    def isEmpty(self):
        return len(self.fila) == 0

    def size(self):
        return len(self.fila)

    def __str__(self):
        return str(self.fila)
    
    def __iter__(self):
        return iter(self.fila)

def verifica_tempo():
    fila = Fila()
    posicao_joao = 22
    posicao_atual = 8
    tempo_total = 60
    tempo_por_pessoa = 4

    for i in range(posicao_atual, posicao_joao + 1):
        fila.queue(i)

    pessoas_na_frente = posicao_joao - posicao_atual

    while not fila.isEmpty():
        pessoa = fila.dequeue()
        if pessoa == posicao_joao:
            break 
        tempo_total -= tempo_por_pessoa

    print(f"João tem {pessoas_na_frente} pessoas na frente.")
    print(f"Tempo estimado de espera: {pessoas_na_frente * tempo_por_pessoa} minutos.")
    print(f"Tempo restante: ", tempo_total, " minutos")

    if tempo_total >= 4:
        print("João será atendido a tempo.")
    else:
        print("João deve voltar em outro horário.")

verifica_tempo()