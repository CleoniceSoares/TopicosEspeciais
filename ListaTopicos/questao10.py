# questao 10
# (Adaptado – Python Zumbi) Escreva um programa para calcular a redução de tempo de vida de um fumante. Considere que para cada cigarro fumado por dia, durante o tempo em anos que ele tem o hábito de fumar, ele perdeu 10 minutos de sua vida. Dessa forma, exiba para o usuário o tempo de vida perdido com o hábito do fumo.
qtd_cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos fumando: "))
total_cigarros = (anos_fumando * 365)*qtd_cigarros
tempo_perdido = (total_cigarros * 10)/24
print ('Tempo de vida perdido: %d dias' %tempo_perdido )
