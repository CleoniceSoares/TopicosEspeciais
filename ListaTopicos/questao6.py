# questao 6
'''Crie um programa para descobrir o custo total de um pedido de pizza, incluindo
os impostos sobre. Suponha que estamos pedindo uma ou mais pizzas do mesmo preço,
e que estamos fazendo o pedido da cidade de Campina Grande. Há um imposto sobre as
vendas que não está incluído no preço do cardápio, mas que será adicionado ao preço
final da compra. A taxa é de 8%, isso significa que é necessário adicionar esse
percentual ao valor final do pedido. Modele o programa da seguinte maneira: 
        a) Pergunte ao cliente quantas pizza ele irá pedir; 
        b) Pergunte o preço da pizza que está no cardápio; 
        c) Calcule o custo total das pizzas sem o imposto; 
        d) Calcule o valor do imposto; 
        e) Calcule o total cobrado da venda incluindo o imposto; 
        f) Mostre ao cliente o valor que será cobrado.                          '''
qtd_pizzas = int(input("Digite a quantidade de pizzas voce vai pedir: "))
preco_pizza = float(input("Digite o preco da pizza que esta no cardapio: "))
total_pizza_sem_imposto = qtd_pizzas*preco_pizza
valor_imposto = (total_pizza_sem_imposto*8)/100
valor_total = total_pizza_sem_imposto+valor_imposto
print("Valor cobrado: %.2f" %(valor_total))
