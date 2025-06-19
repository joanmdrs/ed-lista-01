class Pilha:
    def __init__(self):
        self.itens_pilha = []

    def push(self, item):
        self.itens_pilha.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.itens_pilha.pop()
        raise IndexError("Tentativa de pop em pilha vazia")

    def top(self):
        if not self.isEmpty():
            return self.itens_pilha[-1]
        raise IndexError("Tentativa de top em pilha vazia")

    def isEmpty(self):
        return len(self.itens_pilha) == 0

    def size(self):
        return len(self.itens_pilha)

    def __str__(self):
        return str(self.itens_pilha)


class FilaComPilhas:
    """Criação de duas estruturas pilha para que seja possível simular o funcionamento da FILA."""
    def __init__(self):
        self.entrada = Pilha()
        self.saida = Pilha()

    """Adição de elemento a pilha 'entrada'"""
    def queue(self, item):
        self.entrada.push(item)

    """
    Remoção de um elemento seguindo o comportamento de uma FILA.
    
    No primeiro condicional, caso a pilha 'saida' esteja vazia, é executado o preenchimento
    da pilha 'saida' com os elementos da pilha 'entrada', invertendo assim a ordem dos elementos.
    
    Para isso, é executado um while que repete enquanto a pilha 'entrada' não estiver vazia,
    transferindo os elementos um a um da pilha 'entrada' para a pilha 'saida' usando as operações
    de pop() e push(). Esse processo garante que o elemento mais antigo (o primeiro a entrar na fila)
    fique no topo da pilha 'saida', permitindo a remoção correta no estilo FIFO.
    
    Em seguida, o método remove o topo da pilha 'saida' com pop(), que corresponde ao primeiro
    elemento da fila. Caso ambas as pilhas estejam vazias, é levantada uma exceção indicando
    tentativa de remoção em fila vazia.
    """
    def dequeue(self):
        if self.saida.isEmpty():
            while not self.entrada.isEmpty():
                self.saida.push(self.entrada.pop())
        if self.saida.isEmpty():
            raise IndexError("Tentativa de Dequeue em fila vazia")
        return self.saida.pop()

    """Retorna o elemento na frente da fila. Para simular esse comportamento, é usado a mesma lógica implementada no método dequeue."""
    def peek(self):
        if self.saida.isEmpty():
            while not self.entrada.isEmpty():
                self.saida.push(self.entrada.pop())
        if self.saida.isEmpty():
            raise IndexError("Tentativa de Peek em fila vazia")
        return self.saida.top()

    """A Fila só estará vazia no caso de ambas as pilhas, 'entrada' e 'saida' estiverem vazias."""
    def isEmpty(self):
        return self.entrada.isEmpty() and self.saida.isEmpty()

    """A quantidade de elementos da FILA será correspondente a soma dos tamanhos das pilhas 'entrada' e 'saida'."""
    def size(self):
        return self.entrada.size() + self.saida.size()

    def status(self):
        print("Pilha de entrada:", self.entrada)
        print("Pilha de saída:", self.saida)
        
print(">>> INICIANDO SIMULAÇÃO DA FILA USANDO DUAS PILHAS <<<\n")

fila = FilaComPilhas()

print("Adicionando 1 à fila")
fila.queue(1)
fila.status()

print("\nAdicionando 2 à fila")
fila.queue(2)
fila.status()

print("\nAdicionando 3 à fila")
fila.queue(3)
fila.status()

print("\nVisualizando o primeiro elemento (peek):")
print("Primeiro da fila:", fila.peek())

print("\nRemovendo um elemento da fila (dequeue):")
print("Removido:", fila.dequeue())
fila.status()

print("\nRemovendo mais um elemento da fila:")
print("Removido:", fila.dequeue())
fila.status()

print("\nAdicionando 4 à fila")
fila.queue(4)
fila.status()

print("\nVisualizando o primeiro elemento novamente:")
print("Primeiro da fila:", fila.peek())

print("\nRemovendo todos os elementos restantes:")
while not fila.isEmpty():
    print("Removido:", fila.dequeue())
    fila.status()

print("\nTentando remover de uma fila vazia:")
try:
    fila.dequeue()
except IndexError as e:
    print("Erro:", e)

