#Feito por Bruno Sales
#Agenda eletronica


#Flag mantendo loop do programa
programaAtivo = True

#vetor das atividades
minhasAtividades = []


while programaAtivo :
    
    print("\n --- Menu de Opcoes --- \n")
    print("1- Exibir minha lista de atividades")
    print("2- Incluir um item na minha lista de atividades")
    print("3- Remover um item na minha lista de atividades")
    print("4- Marcar um item da minha lista como Feito")
    print("5- Sair do programa")

    #Entrada da opcao pelo usuario
    #apenas int
    opcao = 0
    
    try : #Aceitar apenas numeros
        opcao = int(raw_input("Informe sua opcao: "))
    except:
        opcao = 0
        
    if(opcao == 1): #Exibir atividades

        #Caso nao haja atividade cadastrada
        if not minhasAtividades:
            print("\n Nao ha atividade cadastrada")
            
        #havendo atividades
        else:    
            print("\n Minhas atividades")
            
            for contador, atividade in enumerate(minhasAtividades):
                print str(contador+1),": ",atividade
        
    elif(opcao == 2): #Adicionar atividades
        
        novaAtividade = raw_input("Informe sua nova atividade: ")
        
        #Adiciondo ao vetor
        minhasAtividades.append(novaAtividade)
        print "\nAtividade ",novaAtividade," adicionada\n"
        
    elif(opcao == 3): #Remover atividades

        #Caso nao haja atividade cadastrada
        if not minhasAtividades:
            print "\n Nao ha atividade cadastrada\n"
            
        #havendo atividades
        else:
            try :
                idAtividadeRemover = int(raw_input("Informe o ID da tarefa a ser removida: ")) - 1

                if idAtividadeRemover + 1 > len(minhasAtividades):
                    print "\n Atividade nao existe\n"
                else:
                    del minhasAtividades[idAtividadeRemover]
                    print "\n Atividade removida\n"
                
            except:
                print "\n Nao foi possivel remover com esse ID\n"
                
    elif(opcao == 4): #Marcar como feita
        
        #Caso nao haja atividade cadastrada
        if not minhasAtividades:
            print "\n Nao ha atividade cadastrada\n"
            
        #havendo atividades
        else:
            try :
                idAtividadeFeita = int(raw_input("Informe o ID da tarefa a ser dada como feita: ")) - 1

                if idAtividadeFeita + 1 > len(minhasAtividades):
                    print "\n Atividade nao existe\n"
                else:
                    atividade = minhasAtividades[idAtividadeFeita]            
                    minhasAtividades[idAtividadeFeita] = "[FEITO] "+ atividade
                    print "\n Atividade ",atividade," marcada como FEITA \n"
            except:
                print "\n Nao foi possivel marcar esse ID como feito\n"
        
    elif(opcao == 5): #Sair do programa
        
        print "\nPrograma sendo encerrado\n"
        programaAtivo = False
        
    else:
        print "Essa opcao nao existe no menu\n";
    
