# questao 7
'''Escreva um algoritmo que calcule o fatorial de um número inteiro lido.
Considere que para calcular o fatorial de um número N a seguinte operação
é obedecida: 
    N!  = 1 x 2 x 3 x ... x N-1 x N,  portanto 3! = 1 x 2 x 3 = 6; e 0!  = 1. '''
n = int(input())
n_fatorial = 1
for i in range(2,n+1):
        n_fatorial = n_fatorial * i
print("%d! = %d" %(n, n_fatorial)) 
