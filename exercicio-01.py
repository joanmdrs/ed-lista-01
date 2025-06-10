# 1. Inventário de Itens com Restrições
# Implemente um sistema que permita cadastrar produtos com os campos: nome, quantidade, categoria e preço.
# - Nome não pode se repetir
# - Quantidade e preço devem ser positivos
# Sem uso de dict ou set. Use apenas listas e funções.

# Decidi separar o código em duas classes. A classe Produto que representa os dados de um produto. E a classe Inventário que contém a lógica da funcionalidade de cadastro.

# Classe que define a instância de Produto
class Produto: 
    def __init__(self, nome, quantidade, categoria, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
        self.preco = preco

# Classe Inventario, responsável pela lógica de funcionamento do método cadastrar_produto
class Inventario:
    # Como no exercício pede para usar apenas estruturas de listas, optei por inicializar uma lista vazia, a qual é preenchida conforme as chamadas ao método cadastrar_produto. 
    def __init__(self):
        self.produtos = []
        
    # O método cadastrar produto recebe como parâmetro os atributos nome, quantidade, categoria e preco
    def cadastrar_produto(self, nome, quantidade, categoria, preco):
        # Ao chamar o método, o mesmo realiza uma varredura na lista, e verifica a cada iteração se o nome fornecido já pertence a alguma instância da classe Produto. 
        for p in self.produtos:
            if p.nome == nome:
                # Caso o nome já tenha sido utilizado, o método retorna uma mensagem de aviso e finaliza a execução.
                print("O nome deste produto já existe na base de dados.")
                return
            
        # Verifica se o parâmetro quantidade é positivo, caso não, retorna uma mensagem de aviso e finaliza a execução do método.
        if quantidade <= 0:
            print("O valor da quantidade informada é inválido.")
            return
        
        # Verifica se o parâmetro preço é positivo, caso não, retorna uma mensagem de aviso e finaliza a execução do método. 
        if preco <= 0:
            print("O valor do preço informado é inválido.")
            return
        
        # Caso os parâmetros tenham passado por todas as verificações, é criado uma instância da classe Produto, utilizando os parâmetros fornecido. 
        produto = Produto(nome, quantidade, categoria, preco)
        # Após criar a instância de Produto, a mesma é adicionada a lista de produtos e exibido uma mensagem de confirmação. 
        self.produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso.")
    
    # O método listar produtos, realiza uma varredura na lista de produtos, e exibe as informações dos objetos Produto. Mas, antes disso, verifica se a lista não é vazia, utilizando o método len para verificar a quantidade de itens presentes na lista. 
    def listar_produtos(self):
        if (len(self.produtos)) == 0:
            print("Não há produtos cadastrados")
        
        for p in self.produtos:
            print(f"- {p.nome} | Quantidade: {p.quantidade} | Categoria: {p.categoria} | Preço: R${p.preco:.2f}")
            
# Define uma instância da classe Inventário 
inventario = Inventario()

# Por meio da variável inventario, ocorre a chamada ao método cadastrar_produto, passando os parâmetros corretos para realização do cadastro, onde é exibida a mensagem "Produto 'Monitor Gamer' cadastrado com sucesso."
inventario.cadastrar_produto(nome="Monitor Gamer", quantidade=2, categoria="Eletrônico", preco=571.33)

# O método cadastrar_produto é chamado novamente, mas dessa vez, informando uma quantidade negativa, resultando no não cadastro do produto, e exibindo a seguinte mensagem "O valor da quantidade informada é inválido."
inventario.cadastrar_produto(nome="Placa de Vídeo RTX 3060", quantidade=-5, categoria="Eletrônicos", preco=1339.90)

# O método cadastrar_produto é chamado novamente, mas dessa vez, informando um preço negativo, resultando no não cadastro do produto, e exibindo a seguinte mensagem "O valor do preço informado é inválido."
inventario.cadastrar_produto(nome="Fone de Ouvido JBL", quantidade=2, categoria="Acessórios", preco=-159.0)

# O método cadastrar_produto é chamado novamente, mas dessa vez, informando o mesmo nome de um produto já cadastrado. O método vai exibir a mensagem "O nome deste produto já existe na base de dados.", e encerrar a execução.
inventario.cadastrar_produto(nome="Monitor Gamer", quantidade=2, categoria="Eletrônico", preco=571.33)

# O método listar_produtos é chamado e é realizado a exibição das informações dos produtos presentes na lista. 
inventario.listar_produtos()
            
            
        

        
        
    
