import unicodedata

def limpar_texto(texto):
    # Normaliza o texto (NFD separa letras dos acentos)
    texto = unicodedata.normalize('NFD', texto)

    # Remove os caracteres de acento (categoria 'Mn' = Mark, nonspacing)
    texto_sem_acentos = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    # Converte para minúsculo e remove tudo que não for alfanumérico
    texto_limpo = ''.join(c.lower() for c in texto_sem_acentos if c.isalnum())

    return texto_limpo

class Pilha:
    def __init__(self):
        self.palindromo = []

    def push(self, item):
        self.palindromo.append(item)

    def pop(self):
        return self.palindromo.pop()
        
    def is_palindromo(self, string):
        
        for s in string:
            self.push(s)
            
        copia = self.palindromo[:]       
        original = self.palindromo[:]  

        for i in original:
            if i != copia.pop():
                return False
        return True
        
class Deque:
    def __init__(self):
        self.palindromo = []

    def pushFront(self, item):
        self.palindromo.insert(0, item)

    def pushBack(self, item):
        self.palindromo.append(item)

    def popFront(self):
        return self.palindromo.pop(0)

    def popBack(self):
        return self.palindromo.pop()

    def front(self):
        return self.palindromo[0]

    def back(self):
        return self.palindromo[-1]

    def size(self):
        return len(self.palindromo)
    
    def is_palindromo(self, string):
        
        for s in string:
            self.pushBack(s)
            
        while self.size() > 1:
            if self.front() != self.back():
                return False
            self.popFront()
            self.popBack()
        return True

class main:
    
    while True:
        print("Informe 'sair' para encerrar.")
        texto = input("Informe o possível palíndromo: ")

        
        if texto.lower() == 'sair':
            break
        
        texto_limpo = limpar_texto(texto)  
        
        pilha = Pilha()
        resultado_pilha = pilha.is_palindromo(texto_limpo)
        print(f"'{texto}' é palíndromo (pilha)?", resultado_pilha)

        
        deque = Deque()
        resultado_deque = deque.is_palindromo(texto_limpo)
        print(f"'{texto}' é palíndromo (deque)?", resultado_deque)

        
        
        
        
         
        
        