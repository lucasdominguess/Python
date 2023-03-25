
'''O IBGE (Instituto Brasileiro de Geografia e Estatística) desejou realizar uma estatística nas cidades pertencentes 
ao estado do Paraná, verificando dados sobre acidentes de trânsito. Neste estudo, precisava-se obter alguns dados,
 que podemos verificar abaixo:

código da cidade;
número de veículos de passeio;
número de acidentes de trânsito com vítimas.
Desejava-se saber ainda:

qual o maior e o menor índice de acidentes de trânsito e a que cidades pertencem;
qual a média de veículos nas cidades juntas;
qual a média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio.
Analisando, assim, o nosso caso problematizador, você, aluno(a), deverá realizar um algoritmo que resolva este problema. Utilize-se de todos os conceitos aprendidos até o presente momento. Bom trabalho.

'''
# cria as listas para armazenar as informações de cada cidade
cidades = []
veiculos = []
acidentes = []
media_acidentes = 'nenhuma cidade teve registro de menos de 2000 veiculos'
# solicita os dados de cada cidade ao usuário
for i in range(3):
    print(f"\nCidade {i+1}:")
    codigo = input("Código da cidade: ")
    veic = int(input("Número de veículos de passeio: "))
    ac = int(input("Número de acidentes de trânsito com vítimas: "))
    
    # adiciona os dados à lista correspondente
    cidades.append(codigo)
    veiculos.append(veic)
    acidentes.append(ac)

# calcula o maior e o menor índice de acidentes e a que cidades pertencem
maior_indice = max(acidentes)
menor_indice = min(acidentes)
cidade_maior = cidades[acidentes.index(maior_indice)]
cidade_menor = cidades[acidentes.index(menor_indice)]

# calcula a média de veículos nas cidades juntas
media_veiculos = sum(veiculos) / len(veiculos)

# calcula a média de acidentes nas cidades com menos de 2000 veículos
if (len(veiculos)) >= 2000:
    contador = 0
    soma_acidentes = 0
    for i in range(len(veiculos)):
        if veiculos[i] < 2000:
            contador += 1
            soma_acidentes += acidentes[i]
            media_acidentes = soma_acidentes / contador
  


# exibe os resultados
print("\nResultados:")
print(f"Maior índice de acidentes: {maior_indice}, cidade {cidade_maior}")
print(f"Menor índice de acidentes: {menor_indice}, cidade {cidade_menor}")
print(f"Média de veículos nas cidades: {media_veiculos}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes}")
