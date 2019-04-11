# questao 9
# Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.
n = int(input())
aux = 1
soma = 0
while(aux<=n):
    soma = soma+aux;
    aux = aux+1;
print(soma)
