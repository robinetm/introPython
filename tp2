# crée par mathis robinet
# crée le 22-09-26
# TP2
import random
rejouer = input(str("veux-tu faire une partie \n oui , non: "))     #demande si le joueur veux faire une partie si il dit oui il commence une partie et si il dit non le code s'arrete

while rejouer =="oui":                          #continue le jeu jusqu'a la personne dit non
    print("Le jeu de la devinette:")            #ecris le nom du jeu
    regle = input(str("Veux-tu savoir les règles du jeu \n oui , non: "))           #demande si le joueur veut savoir les règles

    if regle == ("oui"):                                #si le joueur veut savoir les regles sa écris les règles sinon sa passe les regles et va directe au jeu
        print("Les règles du jeu de la devinette: "
              "\n un nombre entier aléatoire est choisis entre 1 et 1000 et tu dois le deviner. "
              "\n À chaque erreur il y est afficher si le nombre écris est plus petit , plus grand ou égale que le nombre mystère. "
              "\n Plus tu fais d'erreur plus ton nombre d'essaie diminue et tu as 10 essaie")

    chiffre_aleatoire = random.randint(1, 1000)         #génère le chiffre mystère
    nbrEssaie = 11                                    #définie le nombre d'essaie du joueur

    while nbrEssaie != 0:           #continue jusqu'a le nombre d'essaie = a 0
        essaie = input("\n écris un nombre entier entre 1 et 1000 tu a %d essaie: "%(nbrEssaie))           #le joueur doit écrire un nombre entre 1 et 1000
        essaieINT = int(essaie)             #transforme la variable "essaie" en intager

        if essaieINT > chiffre_aleatoire:                     #si l'essaie est plus grand que le chiffre mystère sa dit que le le nombre mystère est plus petit
            print("Le nombre mystère est plus petit")

        elif essaieINT < chiffre_aleatoire:                   #si l'essaie est plus petit que le chiffre mystère sa dit que le le nombre mystère est plus grand
            print("Le nombre mystère est plus grand")

        elif essaieINT == chiffre_aleatoire:                  #si l'essaie est égale au chiffre mystère sa écris "Bravo vous avez trouvé le nombre mystère" en escalier et sort de la boucle while
            for i in range(50):
                print(i * " " + "Bravo vous avez trouvé le nombre mystère.")
            break

        if essaieINT != chiffre_aleatoire :                   #si l'essaie n'égal pas au chiffre mystere le nombre d'essaie diminue de 1
            nbrEssaie = nbrEssaie-1

        if nbrEssaie == 0:                                                                                  #si le nombre d'essaie est égale a 0 sa dit que le joueur a perdu
            print("tu n'as pas réussie a trouver le nombre %d,tu as perdu."%(chiffre_aleatoire))

    rejouer = input(str("veux-tu refaire un partie \n oui , non: "))  #quand la partie est finis sa demande au joueur si il veu refaire une partie si il dit oui sa refais une partie et si il dit non la code s'arrete





