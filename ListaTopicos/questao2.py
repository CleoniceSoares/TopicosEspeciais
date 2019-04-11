# questão 2
#Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
qtd = 0
for i in range(1,7):
    n = float(input())
    if n > 0:
        qtd = qtd + 1
print (qtd)
