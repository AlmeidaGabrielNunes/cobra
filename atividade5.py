valores = [] ##vetor 

for i in range(3): 

    valor = int(input(f"Digite o {i+1}º valor inteiro: ")) 

    valores.append(valor) ##adiciona o valor no array 

for i in range(len(valores) - 1): 

    for j in range(i + 1, len(valores)): 

        if valores[i] < valores[j]:

            valores[i], valores[j] = valores[j], valores[i] #ordenanando  


print("Valores em ordem decrescente:", end=" ") 

for valor in valores: 

    print(valor, end=" ") ##end= é pra n pular linha, mas dar um espaço  