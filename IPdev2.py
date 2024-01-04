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