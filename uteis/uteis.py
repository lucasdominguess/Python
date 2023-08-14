#Exemplo de como chamar função : 
#1.import uteis / para chamar digita : uteis.'NomedaFunção'
#2.from uteis import 'nomedaFunção1','nomedaFunção2'/ digita apenas 'nomedaFunção'

def mostraLinha(): #criar linha
    linha = ( 10*'---')
    return linha

def somaSimples(a,b): #somar somente a + b 
    s=a+b 
    print (s)

def somaValores(*valores):  # somar varios valores sem qtd definida 
    s=0 
    for num in valores: 
        s+=num
    print (f'a soma dos valores {valores} temos {s}') 
    #ex entrada: soma(2,5,4,5,8) / saida: 2, 5, 4, 5, 8) temos 24


def tabuadaSimples(): #tabuada de apenas 1 numero
    
    num=int (input('Digite um numero para versmos sua tabuada '))
    for n in range (11):
        print(f'{num} x {n} = {num*n}')

def contagemRegressiva(): #necessario import sleep 
    for i in range(10,-1,-1) : #adcionar o -1 para contar de traz para frente 
        print (i)
        sleep(1)


def valorAcordo(valorInicial):
    mostralinha = 10*'---'
    part_adv = valorInicial * 30/100 
    valorfinal = valorInicial-part_adv
    
    return print (f'{mostralinha} \n O valor do acordo R$ {valorInicial:.2f} \n valor da parte do advogado R${part_adv:.2f} \n sobrara R${valorfinal:.2f} \n {mostralinha}')