a = float(input("Digite o valor do lado a: "))  

b = float(input("Digite o valor do lado b: "))  

c = float(input("Digite o valor do lado c: "))  

areatriangulo = a * b /2  

if (a + b < c) or (a + c < b) or (b + c < a):  

    print("Não é um triângulo")  

else:  

    print('A área do triângulo é: ',areatriangulo) 