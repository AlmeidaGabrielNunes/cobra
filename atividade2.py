#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro 
#vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, 
#o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor. 
salfix = float(input('Digite o valor do salário fixo ')) #o vendedor tem um salário fixo
carrosvendidos = int(input('Digite quantos carros o funcionário vendeu ')) 
comissaoporcarro = float(input('Digite o valor fixo por carro vendido ')) #ele tem uma comissao relacionada a quantidade de carros vendidos
valortotaldevenda = float(input('Digite quanto o vendedor vendeu ')) #ele ganha 5% em cima do valor total das vendas. 
cincoporcento = valortotaldevenda * 0.05 #aqui são os 5% em cima do valor total de vendas
comissaototal = comissaoporcarro * carrosvendidos #aqui é a comissão por quantidade de carros
salariofinal = comissaototal + cincoporcento + salfix 

print("O salario final é :", salariofinal)