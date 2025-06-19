class Pilha:
    def __init__(self):
        self.itens_pilha = []

    def push(self, item):
        print("\nAdicionando elemento à pilha")
        self.itens_pilha.append(item)

    def pop(self):
        print("\nRemovendo elemento da pilha")
        if not self.isEmpty():
            self.itens_pilha.pop()
        else:
            print("Erro: pilha vazia")

    def top(self):
        print("\nRetornando elemento do topo da pilha sem removê-lo")
        return self.itens_pilha[-1]

    def isEmpty(self):
        print("\nVerificando se a pilha está vazia")
        return len(self.itens_pilha) == 0

    def size(self):
        print("\nRetornando quantidade de elementos da pilha")
        return len(self.itens_pilha)

    def status(self):
        print("Estado da pilha:", self.itens_pilha)


class Fila:
    def __init__(self):
        self.itens_fila = []

    def queue(self, item):
        print("\nAdicionando elemento à fila")
        self.itens_fila.append(item)

    def dequeue(self):
        print("\nRemovendo elemento da fila")
        if not self.isEmpty():
            return self.itens_fila.pop(0)
        print("Erro: fila vazia")

    def peek(self):
        print("\nRetornando primeiro elemento da fila sem removê-lo")
        if not self.isEmpty():
            return self.itens_fila[0]
        print("Erro: fila vazia")

    def isEmpty(self):
        print("\nVerificando se a fila está vazia")
        return len(self.itens_fila) == 0

    def size(self):
        print("\nRetornando quantidade de elementos da fila")
        return len(self.itens_fila)

    def status(self):
        print("Estado da fila:", self.itens_fila)


class Deque:
    def __init__(self):
        self.itens_deque = []

    def pushFront(self, item):
        print("\nAdicionando elemento no início do deque")
        self.itens_deque.insert(0, item)

    def pushBack(self, item):
        print("\nAdicionando elemento no final do deque")
        self.itens_deque.append(item)

    def popFront(self):
        print("\nRemovendo elemento do início do deque")
        if not self.isEmpty():
            return self.itens_deque.pop(0)
        print("Erro: deque vazio")

    def popBack(self):
        print("\nRemovendo elemento do final do deque")
        if not self.isEmpty():
            return self.itens_deque.pop()
        print("Erro: deque vazio")

    def front(self):
        print("\nRetornando primeiro elemento do deque sem removê-lo")
        if not self.isEmpty():
            return self.itens_deque[0]
        print("Erro: deque vazio")

    def back(self):
        print("\nRetornando último elemento do deque sem removê-lo")
        if not self.isEmpty():
            return self.itens_deque[-1]
        print("Erro: deque vazio")

    def isEmpty(self):
        print("\nVerificando se o deque está vazio")
        return len(self.itens_deque) == 0

    def size(self):
        print("\nRetornando quantidade de elementos do deque")
        return len(self.itens_deque)

    def status(self):
        print("Estado do deque:", self.itens_deque)


print("EXECUÇÃO DA CLASSE PILHA")
pilha = Pilha()
pilha.push(10)
pilha.status()
pilha.push(5)
pilha.status()
print(pilha.top())
print(pilha.isEmpty())
print(pilha.size())
pilha.pop()
pilha.status()
pilha.pop()
pilha.status()

print("\n\nEXECUÇÃO DA CLASSE FILA")
fila = Fila()
fila.queue(10)
fila.status()
fila.queue(20)
fila.status()
print(fila.peek())
print(fila.isEmpty())
print(fila.size())
fila.dequeue()
fila.status()
fila.dequeue()
fila.status()

print("\n\nEXECUÇÃO DA CLASSE DEQUE")
deque = Deque()
deque.pushBack(30)
deque.status()
deque.pushFront(40)
deque.status()
deque.pushBack(50)
deque.status()
print(deque.front())
print(deque.back())
print(deque.isEmpty())
print(deque.size())
deque.popFront()
deque.status()
deque.popBack()
deque.status()
deque.popFront()
deque.status()
