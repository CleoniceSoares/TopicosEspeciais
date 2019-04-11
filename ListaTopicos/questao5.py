# questao 5
# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
qtd_positivos = 0
total = 0
for i in range(1,7):
    n = float(input())
    if n > 0:
        qtd_positivos = qtd_positivos + 1
        total = total + n
media = total/qtd_positivos
print(qtd_positivos)
print("%.1f" %(media))
