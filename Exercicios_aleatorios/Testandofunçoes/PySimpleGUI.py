import PySimpleGUI as sg
import requests

def pegar_cotacoes(codigo_moeda): #Função de exemplo para test 
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None
    
#sg.theme('DarkAmber')   # Adicione um pouco de cor às suas janelas
# All the stuff inside your window. This is the PSG magic code compactor...
'''
Padrao documentação 
layout = [  [sg.Text('Pegar contação da Moeda')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]
'''
layout = [ 
        [sg.Text('Pegar contação da moeda')],
        [sg.InputText()],
        [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
        [sg.Text("A cotação foi de ")],
]

# Criar a Janela 
janela = sg.Window('Window Title', layout)
#Efeito loop 
while True:             
    eventos, valores = janela.read()
    if eventos in (sg.WIN_CLOSED, 'Cancel'):
        break

janela.close()