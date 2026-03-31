import random 
def jogar_impar_par():

    jogo = input("Você é par ou impar?").upper()

    numero= int(input("Agora escolha um número de 1 a 10: "))
    if numero > 10:
        print ("você não tem mais de 10 dedos!")
        exit()

    numero_aleatorio = random.randint(1,10)

    print(f"Eu escolhi {numero_aleatorio}")

    soma= (numero + numero_aleatorio) % 2

    if soma == 0 and jogo == "PAR":
        print(f"O número é par, você ganhou")
    elif soma == 0 and jogo == "IMPAR":
        print(f"O número é par, você perdeu")
    elif jogo == "IMPAR" and soma != 0:
        print(f"O número é ímpar, você ganhou")
    elif jogo == "PAR" and soma !=0:
        print(f"O número é ímpar, você perdeu")

