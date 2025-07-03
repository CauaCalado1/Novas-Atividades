class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def enqueue(self, dado, prioridade):
        item = (prioridade, dado)

        if not self.fila or prioridade < self.fila[0][0]:
            self.fila.insert(0, item)
            return

        for i in range(len(self.fila)):
            p_existente, _ = self.fila[i] 
            
            if prioridade < p_existente:
                self.fila.insert(i, item)
                return
            elif prioridade == p_existente:
                j = i
                while j < len(self.fila) and self.fila[j][0] == prioridade:
                    j += 1
                self.fila.insert(j, item)
                return
        
        self.fila.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")
        return self.fila.pop(0)[1]

    def is_empty(self):
        return len(self.fila) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")
        return self.fila[0][1]

    def size(self):
        return len(self.fila)

    def __str__(self):
        return f"[{', '.join(f'({p}, {d})' for p, d in self.fila)}]"
    
#exemplo

fila_de_tarefas = FilaDePrioridade()

print(" Adicionando tarefas à fila ")

print("Adicionando tarefa do Cauã (Prioridade 3)")
fila_de_tarefas.enqueue("Tarefa do Cauã", 3)
print(f"Fila atual: {fila_de_tarefas}")

print("\nAdicionando tarefa do Breno (Prioridade 1)")
fila_de_tarefas.enqueue("Tarefa do Breno", 1)
print(f"Fila atual: {fila_de_tarefas}")

print("\nAdicionando tarefa do Iago (Prioridade 5)")
fila_de_tarefas.enqueue("Tarefa do Iago", 5)
print(f"Fila atual: {fila_de_tarefas}")


print("\nAdicionando outra tarefa do Cauã (Prioridade 2)")
fila_de_tarefas.enqueue("Outra Tarefa do Cauã", 2)
print(f"Fila atual: {fila_de_tarefas}")


print("\nAdicionando outra tarefa do Breno (Prioridade 3 - mesma do Cauã)")
fila_de_tarefas.enqueue("Outra Tarefa do Breno", 3)
print(f"Fila atual: {fila_de_tarefas}")


print("\n--- Processando tarefas da fila ---")


print(f"\nPróxima tarefa a ser processada (dequeue): {fila_de_tarefas.dequeue()}")
print(f"Fila após dequeue: {fila_de_tarefas}")

print(f"\nPróxima tarefa a ser processada (dequeue): {fila_de_tarefas.dequeue()}")
print(f"Fila após dequeue: {fila_de_tarefas}")


print(f"\nPróxima tarefa a ser processada (dequeue): {fila_de_tarefas.dequeue()}")
print(f"Fila após dequeue: {fila_de_tarefas}")

print(f"\nPróxima tarefa a ser processada (dequeue): {fila_de_tarefas.dequeue()}")
print(f"Fila após dequeue: {fila_de_tarefas}")

print(f"\nPróxima tarefa a ser processada (dequeue): {fila_de_tarefas.dequeue()}")
print(f"Fila após dequeue: {fila_de_tarefas}")

print(f"\nA fila de tarefas está vazia? {fila_de_tarefas.is_empty()}")

try:
    print("\nTentando processar tarefa de uma fila vazia:")
    fila_de_tarefas.dequeue()
except IndexError as e:
    print(f"Erro: {e}")