# -*- coding: utf-8 -*-
"""exercicio-arrays-lista-produtos2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qrOJmg_JpRtoCyqoARlpPIOzSRCKXXWB

A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

Como desafio, adicione dois novos produtos da sua escolha à lista.
"""

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Listagem dos produtos
print(lista_produtos)


#Impressão Lista Nova dos Produtos
lista_produtos.pop()
for i in (lista_produtos):
  lista_produtos[1], lista_produtos[4] = "rímel", "cremes hidratantes"
  print("Temos " + i + " à venda!")