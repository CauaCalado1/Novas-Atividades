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

    def dequeue(self):
        if self.is_empty():
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
            return "[Vazia]"
        
        elementos = []
        atual = self.frente
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "[" + " -> ".join(elementos) + "]"

def simular_batata_quente(lista_nomes, num_passes):
    
    fila_jogadores = Fila()

    # Adiciona todos os nomes à fila
    for nome in lista_nomes:
        fila_jogadores.enqueue(nome)
    
    print(f"Jogadores iniciais: {fila_jogadores}")

    while fila_jogadores.size() > 1:
        print(f"\nNúmero de passes: {num_passes}")
        for _ in range(num_passes):
            jogador_passado = fila_jogadores.dequeue()
            fila_jogadores.enqueue(jogador_passado)
            print(f"  Passou a batata para: {jogador_passado}. Fila atual: {fila_jogadores}")
        
        jogador_eliminado = fila_jogadores.dequeue()
        print(f"!!! {jogador_eliminado} se queimou e saiu do jogo. !!!")
        print(f"Jogadores restantes: {fila_jogadores}")

    vencedor = fila_jogadores.dequeue()
    return vencedor

#exemplos
print(" Simulador do Jogo da Batata Quente ")

nomes_jogo1 = ["Caua", "Breno", "Iago", "Guilherme", "Pedro"]
num_passes_jogo1 = 7
vencedor1 = simular_batata_quente(nomes_jogo1, num_passes_jogo1)
print(f"\n--- VENCEDOR: {vencedor1} ---")

print("\n" + "="*40 + "\n")

