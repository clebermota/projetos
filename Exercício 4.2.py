"""Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
80 km/h."""

velocity = int(input("Qual a velocidade atual do carro?"))
print()

multa = (velocity - 80) * 5
print()

if velocity <= 80:
    print("Boa viagem!")
if velocity > 80:
    print(f"O usuario foi multado por está a {velocity}km/h")
    print()
    print(f"O valor da multá é de R${multa},00")