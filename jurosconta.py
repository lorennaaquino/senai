print("sistema de taxas de juros")
print("desenvolvido por:lorenna aquino")
print("copywrite 2024")
print("versao 1.0")
while True:
    valordaconta= float(input("valor da conta:R$"))
    diasdeatraso= float(input("dias de atraso"))
    jurospordia= float(input( "juros por dia%"))

    valorcorrigido =valordaconta + (valordaconta * diasdeatraso* (jurospordia/100))
    print(f"O valor corrigido é:R${valorcorrigido:.2f}")
    sair=input("deseja corrigir outro valor?<S/N>")
    if sair.upper() == "N":
        break
print("agradeço pela visita,volte sempre!)