import os 
from time import sleep 
salas = ['maria','helena',] , ['elaine',], ['luiz','joao','eduarda' , (0,10,20,30,40)]

print (salas[0][1]) #Saida 'helena' 
#primeiro indice [0] acessa a lista na ordem correspondente .
#segundo indice [1] acessar o item da lista na ordem correspondente . 

print (salas[1][0]) #saida 'elaine'  
#se for 
print (salas[2]) #saida ['luiz','joao','eduarda' , ] 
# se for selecionada apenas um indice , ele exibira a lista completa

print (salas[2][3][3]) #saida 30 
#indicanto tres indices ele busca listas dentro de listas 

print (salas[1][0],salas[2][3][2]) #saida elaine 20 
#usar a virgula para indicar a separação das listas e fazer novo acesso
sleep(3)
os.system('cls')

salas_2 = ['1* Ano ','maria','helena',] , ['2* Ano','elaine',], ['3* ano ', 'luiz','joao','eduarda' ,]

for sala in salas_2 : #exibe todos os nomes dentro das salas
    for aluno in sala:
        print(aluno)

for sala in salas_2 : #exibe todos os nomes dentro das salas
    print (f'existe a sala do {sala[0]}')
    for aluno in sala:
       print(f'que tem o aluno {aluno}')