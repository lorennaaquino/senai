while 1==1:
    peso   =float(input("digite seu peso:"))
    altura =float(input("digite sua altura:"))
    imc=peso/ (altura*altura)
    if imc > 40:
        print("obesidade grau 3")
    elif imc> 35:
        
        print("obesidade grau 2")
    elif imc > 30:
        print("obesidade grau 1")
    elif imc> 25:
        print("sobrepeso")
    elif imc >18.5:
         print("peso normal")
    else:
        print("baixo peso")