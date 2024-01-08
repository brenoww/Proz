# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

nome = input("Insira seu nome completo: \n")

numero = '';
numeroValido = False

while(numeroValido != True):
    numero = int(input("Insira um ano válido (ex.: 2001): \n"))
    if(numero < 2022 and numero >1991):
        numeroValido = True;
        print("Nome: " + nome + "\n")
        print("Idade: " + str(2021 - numero))
    else: 
        print("Ano inválido")