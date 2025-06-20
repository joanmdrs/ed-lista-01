class Fila:
    def __init__(self):
        self.fila = []

    def queue(self, item):
        self.fila.append(item)  
        
    def queue_prioritario(self, item):
        self.fila.insert(0, item)

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

    pessoas_na_frente = 0

    while not fila.isEmpty():
        pessoa = fila.dequeue()

        if pessoa == 14:
            print("João, Estamos na posição 14.")
            print("Acabam de chegar uma gestante e um idoso. É necessário colocá-los no início da fila.")
            print(f"Você tem {tempo_total} minutos restantes. Vamos calcular se é possível esperar.")
            fila.queue_prioritario('gestante')
            fila.queue_prioritario('idoso')

        if pessoa == posicao_joao:
            break
        
        tempo_total -= tempo_por_pessoa
        pessoas_na_frente += 1

    print(f"João, tem {pessoas_na_frente} pessoas na frente (incluindo prioritários).")
    print(f"Tempo total estimado de espera: {pessoas_na_frente * tempo_por_pessoa} minutos.")
    print(f"Tempo restante: {tempo_total} minutos.")

    if tempo_total >= tempo_por_pessoa:
        print("João será atendido a tempo.")
    else:
        print("João deve voltar em outro horário.")

verifica_tempo()