#🔥 Fogo vence Planta → queima
#🌱 Planta vence Água → absorve
#💧 Água vence Fogo → apaga
#Ciclo: Fogo > Planta > Água > Fogo

import random 
print (""" 


  __                                                          _             _        
 / _| ___   __ _  ___      __ _  __ _ _   _  __ _       _ __ | | __ _ _ __ | |_ __ _ 
| |_ / _ \ / _` |/ _ \    / _` |/ _` | | | |/ _` |     | '_ \| |/ _` | '_ \| __/ _` |
|  _| (_) | (_| | (_) |  | (_| | (_| | |_| | (_| |  _  | |_) | | (_| | | | | || (_| |
|_|  \___/ \__, |\___( )  \__,_|\__, |\__,_|\__,_| ( ) | .__/|_|\__,_|_| |_|\__\__,_|
           |___/     |/         |___/              |/  |_|                            """)


print ("Bem vindo(A) ao jogo Fogo, água, planta")

jogador = input ("Escolha qual você quer"). upper()
computador = random.choice (["FOGO, ÁGUA, PLANTA"])
print (f"Eu escolhi {computador}")

if jogador == computador:
    print (f"Deu empate")

elif jogador == FOGO and computador == ÁGUA:
    print ("A minha água apagou o seu fogo")
elif jogador == ÁGUA and computador == FOGO:
    print ("A sua água apagou o meu fogo")
elif jogador == PLANTA and computador == ÁGUA:
    print ("A sua planta ganhou da minha água")
elif jogador == PLANTA and computador == FOGO:
    print ("O meu fogo ganhou da sua planta")
elif jogador == FOGO and computador == PLANTA:
    print ("O seu fogo queimou a minha planta")
elif jogador == ÁGUA and computador == PLANTA: 
    print ("A minha planta ganhou da sua água")