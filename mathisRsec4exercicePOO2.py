#crée par 25/01/2023
#crée le mathis robinet
#exercice POO 2

import arcade
import random
from enum import Enum

#choisis les 3 plus grand lancé de dé automatiquement pour force agilité etc
def lanceDe():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    de3 = random.randint(1, 6)
    de4 = random.randint(1, 6)
    PetitForce = min(de1, de2, de3, de4)
    lanceDe = [de1, de2, de3, de4]
    lanceDe.remove(PetitForce)
    return sum(lanceDe)

#Établie les caracteristique de l'NPC selon les lancé de dé et la réponse du joueur

force= lanceDe()
print(f'force: {force}')
agilite=lanceDe()
print(f'agilite: {agilite}')
constitution=lanceDe()
print(f'constitution: {constitution}')
intelligence=lanceDe()
print(f'intelligence: {intelligence}')
sagesse=lanceDe()
print(f'sagesse: {sagesse}')
charisme=lanceDe()
print(f'charisme: {charisme}')

PV= random.randint(1,20)
armure= random.randint(1,12)
nom= input(str('Quelle est votre nom ?: '))
print(f'Daccord je vous appelerez donc {nom}.')
race= input(str('Quelle est votre race ?: '))
print(f'Vous etes donc un {race}.')
espece= input(str('Quelle est votre espèce ?: '))
print(f'Vous serez alors un/une {espece}.')
profession=input(str('Quelle est votre profession ?: '))
print(f'Votre profession sera {profession}.')

#demande si le joueur veut afficher ses stats
afficherStats= input(f'\nVoulez vous que j affiche vos stats {nom} ? oui,non: ')

if afficherStats == 'oui':
    print(f'\nVoici vos stats {nom}:\nforce:{force}\nagilite:{agilite}\nconstitution:{constitution}\nintelligence:{intelligence}\n'
          f'sagesse:{sagesse}\ncharisme:{charisme}\nPV:{PV}\narmure:{armure}\nnom:{nom}\n race:{race}\nespece:{espece}\n'
          f'profession:{profession}')


#création des classes hero et kobold qui hérite de la classe NPC ayant tout les caracteristique definie plus en haut
class NPC():
    def __init__(self):
        self.force: force
        self.agilite: agilite
        self.constitution: constitution
        self.intelligence: intelligence
        self.sagesse: sagesse
        self.charisme: charisme
        self.PV:PV
        self.armure:armure
        self.nom:nom
        self.race:race
        self.espece:espece
        self.profession:profession
    def afficherStats(self):
        print(f'\nVoici vos stats {nom}:\nforce:{force}\nagilite:{agilite}\nconstitution:{constitution}\nintelligence:{intelligence}\n'
        f'sagesse:{sagesse}\ncharisme:{charisme}\nPV:{PV}\narmure:{armure}\nnom:{nom}\n race:{race}\nespece:{espece}\n'
        f'profession:{profession}')


class hero(NPC):
    def __init__(self):
        super().__init__()
    def attaquer(self):
    def subirATK(self):

class kobold (NPC):
    def __init__(self):
        super().__init__()
    def attaquer(self):
    def subirATK(self):
