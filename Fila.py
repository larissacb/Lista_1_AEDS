class fila:

    def __init__(self):
        self.items = list()
    
    def addFila(self, item):
        self.items.append(item)
        
    def removeFila(self):
        return self.items.pop()

    def getPosicao(self, posicao):
        return self.items[posicao]
    
    def getTamanho(self):
        return len(self.items)
    
    def apagar(self):
        self.items.clear()
