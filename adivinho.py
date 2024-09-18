import random
numero= random.randint(1,20)
print("bem-vindo ao  jogo de adivinhaçao!")
print("tente advinhar o numero que estou pensando entre 1 a 20.")
while True:
    palpite=int(input("de o seu palpite:"))
    if palpite==numero:
        print("puts vc acertou")
        break
    elif palpite>numero:
        print("vc chutou alto")
    else:
        print("vc chutou baixo")
 
