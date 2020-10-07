from Tarefa import tarefa
import re

y = True
tarefas = list()
posicao = list()
pontuacao_ordenada=list()
ano_ordenado=list()
mes_ordenado=list()
dia_ordenado=list()

def menu():
    print("====================================================")
    print('Menu')
    print('1 - Adicionar Tarefa')
    print('2 - Excluir Tarefa')
    print('3 - Informacoes da Tarefa')
    print('4 - Ordenar os dados em ordem crescente para pontuacao')
    print('5 - Ordenar as tarefas pela data de entrega')
    print('0 - Sair')
    print("====================================================")
    x = int(input('Digite um numero: '))
    print("====================================================")
    return x


while y == True:  # loop
    x = menu()
    if x == 1:
        aux = False
        titulo = input("Informe o titulo: ")
        materia = input("Informe a materia: ")
        while (aux == False):
            dia = input("Informe o dia: ")
            if (re.findall('[0-9]+', dia)):
                aux = True
            else:
                print("Opcao invalida")
        aux = False
        while (aux == False):
            mes = input("Informe o mes: ")
            if (re.findall('[0-9]+', mes)):
                aux = True
            else:
                print("Opcao invalida")
        aux = False
        while (aux == False):
            ano = input("Informe o ano: ")
            if (re.findall('[0-9]+', ano)):
                aux = True
            else:
                print("Opcao invalida")
        aux = False
        while (aux == False):
            pontuacao = input("Informe a pontuacao: ")
            if (re.findall('[0-9.]+', pontuacao)):
                aux = True
            else:
                print("Opcao invalida")
        print("====================================================")
        a = tarefa(titulo, materia, int(dia), int(mes), int(ano), float(pontuacao))  # cria um objeto do tipo tarefa
        tarefas.append(a)  # adicono esse objeto a uma lista chamada tarefas

    elif x == 2:
        print("====================================================")
        k = int(input('Digite o numero da Tarefa: '))  # tenho que converter o numero para inteiro pq ele fica salvo como string
        k -= 1  # considero que o usuario digita o numero da tarefa ignorando a posicao 0
        tarefas.pop(k)  # apago o elemento da posicao k da lista. mas esse metodo retorna o valor excluido, coisa que nao e importante
        print("====================================================")
    elif x == 3:
        print("====================================================")
        k = int(input('Digite o numero da Tarefa: '))  # tenho que converter o numero para inteiro pq ele fica salvo como string
        k -= 1  # considero que o usuario digita o numero da tarefa ignorando a posicao 0
        b = tarefas[k]  # b e um objeto
        b.imprimir()  # utilizo o metodo imprimir
        print("====================================================")
    elif x == 4:  # Ordenar os dados em ordem crescente para pontuacao
        pontuacao_ordenada=sorted(tarefas, key=tarefa.getPonto) #ordenando as tarefas pela pontuacao
        print("\nImprimindo as tarefas em ordem crescente de acordo com a pontuacao...")
        for i in range(len(pontuacao_ordenada)):
            c=pontuacao_ordenada[i]
            c.imprimir()
            print("====================================================")
    elif x == 5:  # Ordenar as tarefas pela data de entrega
        i=0
        ano_ordenado=sorted(tarefas, key=tarefa.getAno) #ordenando o ano a partir da lista 'tarefas'
        mes_ordenado=sorted(ano_ordenado, key=tarefa.getMes) #ordenando o mes a partir da lista 'ano_ordenado'
        dia_ordenado=sorted(mes_ordenado, key=tarefa.getDia) #ordenando o dia a partir da lista 'mes_ordenado'
        print("\nImprimindo as tarefas em ordem crescente de acordo com a data de entrega...")
        for i in range(len(dia_ordenado)):
            c=dia_ordenado[i]
            c.imprimir()
    elif x == 0: break
    else: print("Opcao invalida. Digite novamente")
