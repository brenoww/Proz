# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if(operacao == 1):
        res = num1 + num2;
    elif(operacao == 2):
        res = num1 - num2;
    elif(operacao == 3):
        res = num1 * num2;
    elif(operacao == 4):
        res = num1 / num2
    else: res = 0;
    print("%.2f" % res)

num1 = int(input("Informe o primeiro valor:"));
num2 = int(input("Informe o segundo valor:"));
operacao = int(input("Informe o numero da operação:"));

calculadora(num1,num2,operacao);