# crée par mathis robinet
# crée le 22-10-12
# TP3


import arcade
import random




point_de_vie = 20
numero_adversaire=0
nombre_victoires=0
nombre_defaites=0

jouer = input('voulez-vous faire une partie ?')

while jouer == "oui" :
    force_adversaire = random.randint(1, 5)
    print('-----------\n vous tombez face a un adversaire de niveau %d \n------------'%(force_adversaire))  #un adversaire apparait
    choix = int(input('Que voulez-vous faire ?\n'
                      '1- Combattre cet adversaire \n'
                      '2- Contourner cet adversaire et aller ouvrir une autre porte\n'
                      '3- Afficher les règles du jeu\n'
                      '4- Quitter la partie: '))
    if choix == 1 :      #si le choix est un on le joueur combat l'adversaire
        numero_adversaire = numero_adversaire + 1
        de = random.randint(1, 6)

        print('________________________\n'
              'Adversaire : %d\n'
              'Force de l’adversaire : %d\n'
              'Niveau de vie de l’usager : %d\n'
              'Nombre de victoires et de de defaites : %d victoire et %d défaite.\n'
              '_________________________' %
              (numero_adversaire, force_adversaire, point_de_vie, nombre_victoires, nombre_defaites))
        print('vous lancez le dé, vous avez besoin de faire plus que %d pour battre l ennemie'
              %(force_adversaire))
        if force_adversaire < de:
            nombre_victoires = nombre_victoires + 1
            point_de_vie = point_de_vie + force_adversaire
            print('bravo vous avez gagné le combat vous avez fait %d'%(de))
        elif force_adversaire >= de:
            nombre_defaites = nombre_defaites + 1
            point_de_vie = point_de_vie - force_adversaire
            print('malheureusement vous avez perdu le combat vous avez fait %d'%(de))
    if choix ==2:   #si le choix est 2 le joueur contourne l'adversaire
        point_de_vie= point_de_vie -1
        print('vous contournez l ennemie mais vous perdez 1 point de vie, vous avez %d point de vie'%(point_de_vie))
    if choix ==3: #si le choix est 3 sa affiche la regle
        print('\n- Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l adversaire.\n  '
              'Dans ce cas, le niveau de vie de l usager est augmenté de la force de l adversaire.\n'
            '- Une défaite a lieu lorsque la valeur du dé lancé par l usager est inférieure ou égale à\n '
              'la force de l adversaire.  Dans ce cas, le niveau de vie de l usager est diminué de la force de l adversaire.\n'
            '- La partie se termine lorsque les points de vie de l usager tombent sous 0.\n'
            '- L usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n')
    if choix == 4: #si le choix est 4 sa quitte le jeux
        exit()

    if point_de_vie <= 0 :      #si le point de vie est égale ou en dessous de 0 le jeu est fini
        print('vous avez perdue votre vie a atteint 0')
        exit()
