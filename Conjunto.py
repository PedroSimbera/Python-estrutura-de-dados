# Trata-se de uma estrutura padrão que se aplica para vetores e matrizes (lista, dicionário, tupla).
# Destaca-se que tupla e dicionário são formas de listas de certo modo, haja vista que o objetivo é similar.

#Existe outros métodos para verificação de determinados pontos em conjuntos:
# Por exemplo a intersecção (print(set(x.intersection(y)))) | elementos comuns entre os conjuntos
# Diferença (print(set(x.difference(y))))                   | a diferença, elementos que não são iguais
# (print(set(x.symetric_difference(y))))                    | cria um novo conjunto que contém os elementos que estão presentes em x ou em y, mas não em ambos. Em outras palavras, é a diferença simétrica dos conjuntos x e y.
# (print(x.issubset(y))                                     | A função x.issubset(y) retorna True se todos os elementos de x estiverem presentes em y, ou seja, se x for um subconjunto de y. Caso contrário, retorna False.

# SET é para pegar uma lista e trabalhar como um conjunto

#add(elemento):                 | Adiciona um elemento ao conjunto.
# remove(elemento):             | Remove um elemento específico do conjunto. Se o elemento não estiver presente, uma exceção KeyError será lançada.
# discard(elemento):            | Remove um elemento específico do conjunto, se presente. Se o elemento não estiver presente, nenhum erro será lançado.
# clear():                      | Remove todos os elementos do conjunto, deixando-o vazio.
# pop():                        | Remove e retorna um elemento arbitrário do conjunto. Se o conjunto estiver vazio, uma exceção KeyError será lançada.
# copy():                       | Retorna uma cópia rasa (shallow copy) do conjunto.
# union(*conjuntos):            | Retorna um novo conjunto que contém todos os elementos do conjunto atual e dos conjuntos especificados como argumentos.
# intersection(*conjuntos):     | Retorna um novo conjunto que contém apenas os elementos que estão presentes tanto no conjunto atual quanto nos conjuntos especificados.
# issuperset(conjunto):         | Verifica se o conjunto atual é um superconjunto do conjunto especificado.
# isdisjoint(conjunto):         | Verifica se o conjunto atual e o conjunto especificado não têm elementos em comum.

# Alguns dos métodos, existem outros.