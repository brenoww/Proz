# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

print("CALCULADORA \n");

operacao = input("Escolha uma das operações abaixo para calcular:\n\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n\nCaso deseje sair:\n\n0: SAIR\n");

while(operacao != 0):
    
    operacao = str(operacao)
    if(operacao.isdigit()): operacao = int(operacao)

    if operacao in [0,1,2,3,4]:

        if(operacao == 0):
            print("Saindo...") 
            continue;

        num1 = input("Informe o primeiro número\n")
        num2 = input("Informe o segundo número\n")

        if(num1.replace(".","").isnumeric() and num2.replace(".","").isnumeric()):
            num1 = float(num1)
            num2 = float(num2)
        else:
            print("Insira números válidos.");
            continue;

        if(operacao == 1):
            res = num1 + num2;
            print("1: Soma")
        elif(operacao == 2):
            res = num1 - num2;
            print("2: Subtração")
        elif(operacao == 3):
            res = num1 * num2;
            print("3: Multiplicação")
        elif(operacao == 4):
            res = num1 / num2
            print("4: Divisão")
                
        print("\nResultado: %.2f\n\n" % res)        
    else: 
        print("Essa opção não existe.");
    
    input("Pressione 'Enter' para continuar...\n")

    operacao = input("Qual operação deseja executar?\n\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n\nCaso deseje sair:\n\n0: SAIR\n")