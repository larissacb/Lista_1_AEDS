from Tarefa import tarefa

y = True


tarefas=list()
while y==True: #loop
            print('Menu')
            print('1 - Adicionar Tarefa')
            print('2 - Excluir Tarefa')
            print('3 - Informacoes da Tarefa')
            print('0 - Sair')
            x =int(input('\nDigite um numero :' ))


            if x == 1:
                a=tarefa(input('Titulo :'),input('materia :'),int(input('dia :')),int(input('mes :')),int(input('ano :')),float(input('pontuacao :'))) #tarefa é uma classe
                tarefas.append(a) #tarefas é uma lista
                #tarefa[j].adicionar(input('Titulo :'),input('materia :'),input('dia :'),input('mes :'),input('ano :'),input('pontuacao :'))
                #j+=1
                #pass
            elif x == 2:
                k = int(input('Digite o numero da Tarefa')) #tenho que converter o numero para inteiro pq ele fica salvo como string
                k-=1 #considero que o usuario digita o numero da tarefa ignorando a posicao 0
                lixo= tarefas.pop(k) #apago o elemento da posicao k da lista. mas esse metodo retorna o valor excluido, coisa que nao e importante. por isso salvo em lixo
                # tarefa[k-1].excluir(input('Digite o titulo da tarefa :'))
                # k = 1000
                # pass
            elif x == 3:
                k = int(input('Digite o numero da Tarefa'))  # tenho que converter o numero para inteiro pq ele fica salvo como string
                k -= 1  # considero que o usuario digita o numero da tarefa ignorando a posicao 0
                b = tarefas[k] #b e um objeto
                b.imprimir() #utilizo o metodo imprimir
                # l = 1000
                # pass #isso nao existe. o pass e usado para outra coisa
            elif x==0: break
            
            # print(k)
            # print(l)

