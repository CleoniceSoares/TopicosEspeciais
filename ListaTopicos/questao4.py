# questao 4
# Leia 15 valores inteiros. Apresente então o maior valor lido e a posição dentre os 15 valores lidos.
maior = 0
posicao = 0
for i in range(15):
    n = int(input())
    if n>maior:
        maior=n
        posicao=i+1
print (maior)
print (posicao)
