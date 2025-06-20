class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.pilha.pop()
        print("Erro: pilha vazia")   
    
    def isEmpty(self):
        return len(self.pilha) == 0
    
    def size(self):
        return len(self.pilha)
    
    def elementos(self):
        return self.itens_
    
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
    
    
def organizar_elementos(fila):
    pilha_pares = Pilha()
    pilha_ordem = Pilha()
    
    while not fila.isEmpty():
        item = fila.dequeue()
        
        if item % 2 == 0:
            pilha_pares.push(item)
            
    while not pilha_pares.isEmpty():
        pilha_ordem.push(pilha_pares.pop())
        
    while not pilha_ordem.isEmpty():
        fila.queue(pilha_ordem.pop())
        
fila = Fila()

for i in range(10):
    fila.queue(i)
    
print(">>> SIMULAÇÃO DO PROGRAMA <<<")

print("Elementos da Fila original: ", fila)
organizar_elementos(fila)
print("Elementos da Fila final", fila)            
        