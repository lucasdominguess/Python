'''media aritimetica , mostrando media de um aluno  ''' 
nome= (input('digite seu nome'))
nt1 = float (input('Digite a primeira nota '))
nt2 = float (input('Digite a segunda nota ')) 

m = (nt1 + nt2)/2 #nao esquecer () 'ordem de procedencia'  

print (f'a media do aluno {nome} é {m:.1f}') #:.1f sig =Dps do ponto , apenas um digito flutuante