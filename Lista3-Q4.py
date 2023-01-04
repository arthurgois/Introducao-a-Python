#JOGO DA VELHA
import random

dado = [1,2,3,4,5,6]

lanc1 = random.choice(dado)
print("Lance do jogador 1:", lanc1)
lanc2 = random.choice(dado)
print("Lance do jogador 1:", lanc2)

if lanc1 > lanc2:
    print("Jogador 1 comeca")
else:
    print("Jogador 2 comeca")

l1 = [False,False,False]
l2 = [False,False,False]
l3 = [False,False,False]

#incompleto