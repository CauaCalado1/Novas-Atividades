class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):

        if not self.is_empty():
            return self.itens.pop()
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        return None

    def size(self):
        return len(self.itens)

def inverter_string(texto):
    pilha = Pilha()
    
    for caractere in texto:
        pilha.push(caractere)
    
    string_invertida = ""
    while not pilha.is_empty():
        string_invertida += pilha.pop()
        
    return string_invertida


#Aqui deixo dois modelo de entrada

entrada = "Socorra-me subi no onibus em marrocos"
saida = inverter_string(entrada)
print(f"Entrada: \"{entrada}\"")
print(f"Saída: \"{saida}\"")

entrada_2 = "Caua é bonito"
saida_2 = inverter_string(entrada_2)
print(f"Entrada: \"{entrada_2}\"")
print(f"Saída: \"{saida_2}\"")