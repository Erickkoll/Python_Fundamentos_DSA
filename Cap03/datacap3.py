#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios - Métodos e Funções
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      
# In[18]:


def numpar(menor,maior):
    maior += 1
    intervalo = range(menor,maior)
    for i in intervalo:
        if i % 2 == 0:
            print(i)


# In[19]:


numpar(1,20)


# In[ ]:


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string


# In[20]:


def maiusculo(string):
    return string.upper()


# In[21]:


maiusculo('gata')


# In[ ]:


# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista


# In[60]:


lista = [-1,1,3,4]
def add_list(x, y):
    lista = [-1,1,3,4]
    lista.append(x) 
    lista.append(y)
    print(lista)


# In[61]:


add_list(6, 9)


# In[75]:


def lista_4(a,b,c,d):
    lista = [a,b,c,d]
    while len(lista) < 6:
        lista.append(lista[-1]+len(lista)-2)
    print(lista)


# In[76]:


lista_4(1,2,3,4)


# In[52]:


lista = [-1,1,3,4]
lista.append(5)
print(lista)


# In[ ]:


# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos


# In[78]:


def receb(elm,*arg):
    lista = []
    lista.append(elm)
    for item in arg:
        lista.append(item)
    return print(lista)


# In[80]:


receb(3)


# In[81]:


receb(4,6,9,12)


# In[ ]:


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles


# In[85]:


soma = lambda x,y:(x+y)


# In[86]:


soma(4,7)


# In[87]:


# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)


# In[104]:


# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = []
for i in Celsius:
    F = 9/5*i+32
    Fahrenheit.append(F)
print(Fahrenheit)
#print (list(Fahrenheit))


# In[94]:


# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário


# In[95]:


# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
dir(pd)


# In[ ]:


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"
 


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
