from time import sleep

def contagemRegressiva(): #necessario import sleep 
    for i in range(10,-1,-1) : #adcionar o -1 para contar de traz para frente 
        print (i)
        sleep(1)


contagemRegressiva()