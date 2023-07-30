
import sys #Para usar em pasta externa basta copiar caminho do modolo usando \\ 
sys.path.append("D:\\Lucas\\Todos os Cursos\\Python\\Lucas-Domingues_Python\\uteis")
from tkinter import * 
import requests
#primeira opção : Funcionando
import uteis
   
#segunda opção: Funcionando
from uteis import mostraLinha,somaSimples,somaValores


#segunda opção: 


janela = Tk() #Abre janela grafica 
janela.title("testando tkinter") #Titulo da janela 
janela.geometry("400x400") #geometry usado para criar por padrao tamanho total da janela 

                    #Label . usado para criar espaço para texto ser exibido
texto_orientacao = Label(janela,text="Clique no botao para executar o cod")
texto_orientacao.grid(column=0,row=0,padx=5,pady=5) #posição colunas . padx "padding" distancia  
          #grid é usado para editar posiçao do item na tela                                                     
botao=Button(janela,text="Clique aqui agora ",command=mostraLinha)
botao.grid(column=0,row=1,padx=5,pady=5)  #Dica nao passa o parenteses() no final da função , pq isso faz ele ser executado automaticamente

espaco_vazio = Label(janela,text='')
espaco_vazio.grid(column=0,row=2,padx=5,pady=5)

janela.mainloop() #Mantem janela Grafica Aberta
