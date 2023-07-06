'''meu objetivo e criar um jogo simples papel pedra tesoura :) '''
import random


opçoes = ['papel','pedra','tesoura'] 
#pc =random.choice(opçoes)
#entrada = (input ('vamos brincar de Papel , pedra e tesoura? \n Digite S para continuar Digite N para sair ')).upper().strip()

player = (input('Digite papel , pedra ou Tesoura ')).strip()
pc =random.choice(opçoes) #Pc 

if player == 'papel': 
                if  pc == 'pedra':
                      print ('VOCE GANHOU !!!\n vc escolheu papel e o computador escolheu pedra')   
                elif pc == 'tesoura' : 
                        print ('VOCE PERDEU!!! \n Pois escolheu papel e o computador escolheu tesoura' )
                elif player == pc : 
                        print (f'EMPATE!!!! \n voce digitou {player} e o computador {pc}')

elif player == 'pedra' : 
                if pc == 'papel':
                      print ('VOCE PERDEU !!! \n vc escolheu pedra mas o computador escolheu papel')  
                elif pc == 'tesoura' : 
                      print ('VOCE GANHOU !!! \n pois escolheu pedra e o computador escolheu tesoura' )      
                elif player == pc : 
                        print (f'EMPATE!!!! \n voce digitou {player} e o computador {pc}')
                        
elif player == 'tesoura': 
                if pc == 'pedra' : 
                        print ('VOCE PERDEU!!! \n vc escolheu tesoura e o computador escolheu pedra')
                elif pc == 'papel': 
                        print ('VOCE GANHOU!!! \n pois escolheu tesoura e o computador escolheu papel') 
                elif player == pc : 
                        print (f'EMPATE!!!! \n voce digitou {player} e o computador {pc}')

else : 
    print ('Voce nao digitou nenhuma das opçoes! ') 
    
                 











