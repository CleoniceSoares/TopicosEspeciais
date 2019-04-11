# questao 3
# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.
n = int(input())
for i in range(n):
    l1 = input().split()
    a = float(l1[0])
    b = float(l1[1])
    c = float(l1[2])
    media = (a*2+b*3+c*5)/10
    print("%.1f" %(media))
