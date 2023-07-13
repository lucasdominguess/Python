
import sys #Para usar em pasta externa basta copiar caminho do modolo usando \\ 
sys.path.append("D:\\Lucas\\Todos os Cursos\\Python\\Lucas-Domingues_Python\\uteis")

#primeira opção : Funcionando
import uteis
   
#segunda opção: Funcionando
from uteis import mostraLinha,somaSimples,somaValores

uteis.mostraLinha() #primeira opção

uteis.somaSimples(2,6) #primeira opção

#segunda opção: 
mostraLinha()

somaSimples(5,6)

somaValores(5,6,8,9,10)
