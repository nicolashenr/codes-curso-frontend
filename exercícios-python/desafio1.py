print('-'*64)
print('|  ' + ' '*14 +'A Luta Contra o Grande Rei Demônio!' + ' '*10 + ' |')
print('-'*64)

import random

name_hero = str(input('\nDigite o nome do personagem: '))
xp = 0
acertos = 0
xp_pont = 0
enemy_name = 'Grande Rei Demônio da Adivinhação'
enemy_life = 9


print(f'\nSentindo o mundo a beira do colapso...\nO {enemy_name} resolveu atacar!')
print('Sua técnica inválivel de adivinhação é sua única fraqueza...')
print("Será que alguém conseguirá impedi-lo de destruir o mundo?\n")
print(f'\nA aventura de {name_hero} começa agora!\n')

print("\nPara vencer você precisa ADIVINHAR \no mesmo número do Rei Demônio... 3 vezes...\n")

def luta_chef():
    global xp_pont
    acertos = 0
    tentativas = 0
    while True:
        xp_pont += 500
        tentativas += 1
        enemy_hit = random.randint(1, 4)
        hero_attack = int(input('Digite um valor entre 1 e 4: '))
        if hero_attack == enemy_hit:
            print("O Rei Demônio não esperava por essa... continue")
            acertos += 1
            if acertos == 2:
                print("\nEle sentiu seu golpe, sabe que é tudo ou nada!")
            print(f'\nVocê acertou {acertos} golpe no grande rei demônio!\n')
            if acertos == 3:
                print("...por essa ele não esperava...\n")
                print('Triste, ele volta para o inferno...')
                print(f'\n{name_hero} salvou a humanidade!')
                print(f'Você teve {tentativas} tentativas ao total!')
                verifica_pontuacao(xp_pont)
                break
        else:
            print('Ele te olha... tente de novo')
            continue

def verifica_pontuacao(xp_pont):
    print('\nOBS: Quanto mais tentativas, mais pontos você ganha, \nporque o Rei Demônio gosta de jogos...\n')
    print('-'*64)
    print('|  ' + ' '*14 +'A Luta Contra o Grande Rei Demônio!' + ' '*10 + ' |')
    print('-'*64)

    if xp_pont == 1000:
        print('Sua colocação é FERRO!')
    elif 1001 <= xp_pont <= 2000:
        print('Sua colocação é BRONZE!')
    elif 2001 <= xp_pont <= 5000:
        print('Sua colocação é PRATA!')
    elif 5001 <= xp_pont <= 6000:
        print('Sua colocação é OURO!')
    elif 6001 <= xp_pont <= 8000:
        print('Sua colocação é PLATINA DIAMANTE!')
    elif 8001 <= xp_pont <= 9000:
        print('Sua colocação é ASCENDENTE!')
    elif 9001 >= xp_pont <= 10000:
        print("Sua colocação é  IMORTAL!")
    elif xp_port >= 100001:
        print(f"Você é o verdadeiro {enemy_name}")
luta_chef()