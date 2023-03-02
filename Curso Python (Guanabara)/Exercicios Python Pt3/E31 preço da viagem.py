
km_viagem = float (input ('Qual Distancia da viagem?? '))

if km_viagem <= 200 : 
    preço = km_viagem* 0.50 #atençao com o ponto , numero float usa ponto e nao virgula
    print (f'sua viagem é de {km_viagem} e custara R${preço:.2f} ')

elif km_viagem > 200: 
    preço2 = km_viagem*0.45 
    print (f'sua viagem foi mais longa e custava {preço2}')