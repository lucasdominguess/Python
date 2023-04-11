import os
lista_1 = [] 

i = 'I'
a = 'A'
l= 'L'
opção = [] #lista vazia dara continuidade dentro do while 
entrada = input('Deseja iniciar o programa lista de compras? ').upper().strip()

while entrada == 'SIM':
    opção = (input('Selecione uma opção \n [I]nserir \n [A]pagar \n [L]istar \n')).upper().strip()

    #se a opçao dor Inserir 
    if opção == i :
        os.system('cls')
        item = (input ('Digite um item para inserir na lista ')).strip() 
        lista_1.append(item)
        print ('Item:',item,'adcionado a lista')
        entrada = (input('deseja continuar o programa ')).upper()
        if entrada != 'SIM': 
                os.system('cls')
                print ('fim do programa \n LISTA DE COMPRAS : \n',lista_1)
                break 
    #se a opção for apagar itens da lista    
    elif opção == a : 
        os.system('cls')
        remover = (input ('Digite o item que deseja remover da lista ')).strip()
        lista_1.remove(remover)
        print ("Item : ", remover , "Removido!!!")
        entrada = (input('Deseja continuar o programa lista de compras? ')).upper().strip()
        if entrada != 'SIM': 
                print ('fim do programa \n LISTA DE COMPRAS : \n',lista_1)
                break 
    #se a opção for listar (lista todos os itens da lista ate o momento)
    elif opção == l : 
        os.system('cls')
        print ('Segue todos os itens da lista de compras \n ', lista_1)
        entrada = (input('Deseja continuar o programa lista de compras? ')).upper().strip()
        if entrada != 'SIM': 
             print ('fim do programa')
    #caso nenhuma das opçoes acima seja selecionada. 
    else : 
      os.system('cls')
      print ('vc nao digitou nenhuma das opçoes')
      #opção = (input('Selecione uma opção \n [I]nserir \n [A]pagar \n [L]istar \n ')).upper().strip()
      #Nao a a necessidade de inserir 'entrada' , apos o else o programa retorna ao while (entrada)

#print (lista_1)
