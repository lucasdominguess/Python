'''Criando programa para sortear aluno , para mostrar na tela '''
import random

lista = ['ana' , 'maria' , 'pedro' , 'luana',3]

escolhido = random.choice (lista) #usado para ramdomizar o elemento da lista (choices : seleciona o elemento completo ex: ['ana'])

print(escolhido)

random.shuffle(lista) #embaralha a lista 
print (lista)

