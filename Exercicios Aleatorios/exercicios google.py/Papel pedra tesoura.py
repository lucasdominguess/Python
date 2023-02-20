'''meu objetivo e criar um jogo simples papel pedra tesoura :) '''
import random
papel = 'papel'
pedra = 'tesoura'
tesoura = 'pedra'

opçoes = ['papel','pedra','tesoura'] 
pc =random.choice(opçoes)
entrada = (input ('vamos brincar de Papel , pedra e tesoura? \n Digite S para continuar Digite N para sair ')).upper().strip()

while entrada == 'S' :
        player = (input('Digite papel , pedra ou Tesoura'   )).strip()
        if player == 'papel': 
                if  pc == 'pedra':
                      print ('vc ganhou !!! Parabens \n vc escolheu papel e o computador escolheu pedra')   
                if pc == 'tesoura' : 
                        print ('Voce Perdeu !!! \n Pois escolheu papel e o computador escolheu tesoura' )
        if player == 'pedra' : 
                if pc == 'papel':
                      print ('Nao foi dessa vez !!! \n vc escolheu pedra mas o computador escolheu papel')  
                if pc == 'tesoura' : 
                      print ('Parabens voce ganhou !!! \n pois escolheu pedra e o computador escolheu tesoura' )      

        if player == 'tesoura': 
                if pc == 'pedra' : 
                        print ('vc perdeu!!! \n vc escolheu tesoura e o computador escolheu pedra')
                if pc == 'papel': 
                        print ('vc ganhou !!! \n pois escolheu tesoura e o computador escolheu papel') 
                
        
        if player == pc : 
                print (f'EMPATE!!!! \n voce digitou {player} e o computador {pc}')

else : 
                 print ('Voce nao digitou nenhuma das opçoes!  ')
                 entrada = input('Deseja jogar? Digite s para Sim')
        





''''






    if player == pc: 
                print (f'EMPATE!!!! \n voce digitou {player} e o computador {pc}')

    elif  player == 'papel' and pc == 'pedra' :
              print ('vc ganhou !!! Parabens \n vc escolheu papel e o computador escolheu pedra')
    
    elif player == 'papel' and pc == 'tesoura' : 
                print ('Voce Perdeu !!! \n Pois escolheu papel e o computador escolheu tesoura' )

    elif player == 'pedra' and pc == 'tesoura ' : 
            print ('Parabens voce ganhou !!! \n pois escolheu pedra e o computador escolheu tesoura' )

    elif player == 'pedra' and pc == 'papel' : 
             print ('Nao foi dessa vez !!! \n vc escolheu pedra mas o computador escolheu papel') 


    elif player == 'tesoura' and pc == ' papel' : 
             print ('vc ganhou !!! \n pois escolheu tesoura e o computador escolheu papel') 

    elif player == 'tesoura' and pc == ' pedra' : 
             print ('vc perdeu!!! \n vc escolheu tesoura e o computador escolheu pedra')
 #   player = (input('Digite sua esolha , Papel , pedra ou tesoura??'))
else : 
      print ('vc nao digitou nenhuma das opçoes!')
      entrada = input('Deseja jogar? Digite s para Sim')'''