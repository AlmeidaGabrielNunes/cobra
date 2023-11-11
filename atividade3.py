num = int(input('Digite um numero inteiro menor que 1000: ')) 

if num < 1000: 

    centenas = num // 100  ## faz divisão de numero inteiro 230 divido por 100 é 2,3. O // vai pegar só o 2 

    dezenas = (num % 100) // 10 ##aqui vai pegar o resto da divsão e divide o numero inteiro por 100 

    unidades = num % 10 ##aqui só pega o resto da divisão por 10  

    print('{} = {} cetena(s), {} dezena(s) e {}unidade(s)'.format(num, centenas, dezenas, unidades)) 

else: 

    print('Numero maior ou igual a mil') 