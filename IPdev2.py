# Desenvolva um algoritmo que utilize as seguintes características de um veículo:

# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a Melhor veículo informado a partir das condições:


# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.


#Algoritmo:

qtdRodas = int(input("Informe quantas rodas o seu veículo possui:"));
peso = int(input("Informe o peso do veículo:"));
qtdPessoas = int(input("Informe a capacidade do veículo (n° de pesssoas):"));

print("A categoria adequada de CNH é:")
if(qtdRodas == 2 or qtdRodas == 3):
    print("Cat A");
elif (qtdRodas == 4 and qtdPessoas <= 8 and peso <= 3500):
    print("Cat B");
elif (qtdRodas >= 4 and (peso > 3500 and peso <= 6000)):
    print("Cat C");
elif (qtdRodas >= 4 and (qtdPessoas > 8 or peso > 6000)):
    print("Cat D");