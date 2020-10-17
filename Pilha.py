class pilha:

    def __init__(self):
        self.items = list()
        
    def addPilha(self, item):
        self.items.insert(0,item)
    
    def removePilha(self):
        return self.items.pop(0)

    def getPosicao(self, posicao):
        return self.items[posicao]
    
    def getTamanho(self):
        return len(self.items)
    
    def apagar(self):
        self.items.clear()
