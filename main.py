from Tarefa import tarefa
import re

y = True

tarefas=list()
posicao=list()
while y==True: #loop
            print('Menu')
            print('1 - Adicionar Tarefa')
            print('2 - Excluir Tarefa')
            print('3 - Informacoes da Tarefa')
            print('4 - Ordenar os dados em ordem crescente para pontuacao')
            print('5 - Ordenar as tarefas pela data de entrega')
            print('0 - Sair')
            x =int(input('\nDigite um numero :' ))

            if x == 1:
                aux=False
                titulo=input("Informe o titulo: ")
                materia=input("Informe a materia: ")
                while(aux==False):
                    dia=input("Informe o dia: ")
                    if(re.findall('[0-9]+', dia)): aux=True
                    else: print("Opcao invalida")
                aux=False
                while(aux==False):
                    mes=input("Informe o mes: ")
                    if(re.findall('[0-9]+', mes)): aux=True
                    else: print("Opcao invalida")
                aux=False
                while(aux==False):
                    ano=input("Informe o ano: ")
                    if(re.findall('[0-9]+', ano)): aux=True
                    else: print("Opcao invalida")
                aux=False
                while(aux==False):
                    pontuacao=input("Informe a pontuacao: ")
                    if(re.findall('[0-9.]+', pontuacao)): aux=True
                    else: print("Opcao invalida")
                a=tarefa(titulo, materia, int(dia), int(mes), int(ano), float(pontuacao))#cria um objeto do tipo tarefa
                tarefas.append(a) #adicono esse objeto a uma lista chamada tarefas
                    
            elif x == 2:
                k = int(input('Digite o numero da Tarefa')) #tenho que converter o numero para inteiro pq ele fica salvo como string
                k-=1 #considero que o usuario digita o numero da tarefa ignorando a posicao 0
                =====lixo= tarefas.pop(k) #apago o elemento da posicao k da lista. mas esse metodo retorna o valor excluido, coisa que nao e importante. por isso salvo em lixo
            elif x == 3:
                k = int(input('Digite o numero da Tarefa'))  # tenho que converter o numero para inteiro pq ele fica salvo como string
                k -= 1  # considero que o usuario digita o numero da tarefa ignorando a posicao 0
                b = tarefas[k] #b e um objeto
                b.imprimir() #utilizo o metodo imprimir
            elif x==4: #Ordenar os dados em ordem crescente para pontuacao
                for i in range(len(tarefas)):
                    if i==0:
                        pos=tarefas[i].getpontuacao()
                    else:
                        if tarefas[i].getpontuacao()<
            elif x==5:#Ordenar as tarefas pela data de entrega
                
            elif x==0: break

