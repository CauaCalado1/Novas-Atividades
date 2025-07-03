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

class Navegador:
    def __init__(self, pagina_inicial):
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()
        self.pagina_atual = pagina_inicial
        print(f"Iniciando na página: {self.pagina_atual}")

    def visitar_pagina(self, url):
        if self.pagina_atual: # Só adiciona ao histórico de voltar se houver uma página atual
            self.historico_voltar.push(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar = Pilha() # Limpa o histórico de avançar
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.historico_voltar.is_empty():
            self.historico_avancar.push(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
            print(f"Voltando para: {self.pagina_atual}")
        else:
            print("Não há páginas anteriores para voltar.")

    def avancar(self):
        if not self.historico_avancar.is_empty():
            self.historico_voltar.push(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
            print(f"Avançando para: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")

    def exibir_pagina_atual(self):
        print(f"Página atual: {self.pagina_atual}")

# --- Exemplo de Uso ---
print("Navegador")
meu_navegador = Navegador("Paginal Inicial")

meu_navegador.visitar_pagina("google.com")
meu_navegador.visitar_pagina("youtube.com")
meu_navegador.visitar_pagina("github.com")

print("Ação de Voltar")
meu_navegador.voltar() 
meu_navegador.voltar() 
meu_navegador.voltar() 
meu_navegador.voltar() 

print(" Ação de Avançar ")
meu_navegador.avancar() 
meu_navegador.avancar() 
meu_navegador.avancar() 
meu_navegador.avancar() 

print(" Nova Navegação após Voltar")
meu_navegador.voltar()
meu_navegador.visitar_pagina("facebook.com") 
meu_navegador.avancar() 

print("Estado Final ")
meu_navegador.exibir_pagina_atual()