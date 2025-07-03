class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.frente = None  
        self.fim = None     
        self._tamanho = 0

    def enqueue(self, item):
        novo_no = No(item)
        if self.is_empty():
            self.frente = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self._tamanho += 1
        print(f"'{item}' entrou na fila.")

    def dequeue(self):
        
        if self.is_empty():
            print("A fila está vazia. Não há clientes para atender.")
            return None
        
        item_removido = self.frente.dado
        self.frente = self.frente.proximo
        if self.frente is None: 
            self.fim = None
        self._tamanho -= 1
        return item_removido

    def is_empty(self):
        return self.frente is None

    def size(self):
        return self._tamanho

    def peek(self):
        if self.is_empty():
            return None
        return self.frente.dado

    def __str__(self):
        if self.is_empty():
            return "Fila: [Vazia]"
        
        elementos = []
        atual = self.frente
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "Fila: [" + " <- ".join(elementos) + "]"


def novo_cliente(fila, nome_cliente):
    fila.enqueue(nome_cliente)
    print(f"Estado atual da fila: {fila}")

def atender_cliente(fila):
    cliente_atendido = fila.dequeue()
    if cliente_atendido:
        print(f"Atendendo cliente: '{cliente_atendido}'.")
    print(f"Estado atual da fila: {fila}")
    return cliente_atendido

# Exemplo

print(" Simulação de Fila de Atendimento ")
fila_de_atendimento = Fila()

print("\n--- Adicionando primeiros clientes ---")
novo_cliente(fila_de_atendimento, "Marcos")
novo_cliente(fila_de_atendimento, "Gleybson")
novo_cliente(fila_de_atendimento, "Augusto")
novo_cliente(fila_de_atendimento, "Gustavo")


print("\n--- Atendendo o primeiro cliente ---")
atender_cliente(fila_de_atendimento)

print("\n--- Adicionando mais um cliente ---")
novo_cliente(fila_de_atendimento, "Cleiton")

print("\n--- Atendendo clientes restantes ---")
while not fila_de_atendimento.is_empty():
    atender_cliente(fila_de_atendimento)

print("\n--- Tentando atender com fila vazia ---")
atender_cliente(fila_de_atendimento)
