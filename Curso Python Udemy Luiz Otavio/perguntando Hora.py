#faça um programa que pertunte a hora do usuario e dependendo da hora mostre diferentes saudaçoes 


hora = float (input('por favor digite o horario atual ' ))

if hora ==0 or hora <= 11:
    print (f'Agora são {hora:.2f} horas , tenha um bom dia ')
elif hora == 12 or hora <= 18: 
  print (f'Agora são {hora:.2f} horas , tenha uma boa tarde ')
elif hora ==19 or hora <= 23: 
  print (f'Agora são {hora:.2f} horas , tenha uma boa noite ')



print (hora.)