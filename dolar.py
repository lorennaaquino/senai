print("sistema de converção do dólar")
print("desnvolvido por:lorenna aquino")
print("copywrite 2024")
print("versão 1.0")

while True:
    valoremdolar = float(input("valor do produto em dolar: "))
    cotaçãododolarhoje = float(input("digite a cotação do dolar:"))
    valorconvertido = valoremdolar * cotaçãododolarhoje

    print(f"o valor convertido de US${valoremdolar} é R${valorconvertido}")
    sair = input("deseja converter outro valor? <S/N>")
    if sair.upper() == "N":
        break

print( "agradeço pela visita.volte sempre!:-)")

