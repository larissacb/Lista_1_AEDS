class tarefa :

    def __init__(self,nome,materia,dia,mes,ano,ponto):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.ponto = ponto
        self.materia = materia


    def setNome(self,nome):
        self.nome=nome

    def getNome(self):
        return self.nome

    def setDia(self,dia):
        self.dia =dia

    def getDia(self):
        return self.dia

    def setMes(self,mes):
        self.mes=mes

    def getMes(self):
        return self.mes

    def setAno(self,ano):
        self.ano=ano

    def getAno(self):
        return self.ano

    def setPonto(self,ponto):
        self.ponto=ponto

    def getPonto(self):
        return self.ponto

    def setMateria(self,materia):
        self.materia=materia

    def getMateria(self):
        return self.materia

    def imprimir(self):
        print("====================================================")
        print('Titulo :',self.nome)
        print('Materia :',self.materia)
        print('Pontuacao :',self.ponto)
        print('Data :',self.dia,'/',self.mes,'/',self.ano)
        print("====================================================")
