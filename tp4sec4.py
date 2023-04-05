#crée par 2023/03/21
#crée le mathis robinet
#tp4 (cercle bouge/couleur aleatoire)

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_SHAPES = 20

class Forme():
    def __init__(self, width,height,x,y,c,m_x ,m_y,angle):
        self.width = width
        self.height = height
        self.centre_x = x
        self.centre_y = y
        self.angle = angle
        self.color = (c)
        self.delta_x = m_x
        self.delta_y = m_y


# mouvement
    def mouvement(self):
        self.centre_x += self.delta_x
        self.centre_y += self.delta_y

        if self.centre_x < 0 :
            self.delta_x *= -1
        if self.centre_y < 0 :
            self.delta_y *= -1
        if self.centre_x > SCREEN_WIDTH :
            self.delta_x *= -1
        if self.centre_y > SCREEN_HEIGHT :
            self.delta_y *= -1


class cercle(Forme):

    def __init__(self, rayon,x,y,c,m_x ,m_y):
        self.rayon = rayon
        self.centre_x = x
        self.centre_y = y

        self.color = (c)
        self.delta_x = m_x
        self.delta_y = m_y


    def draw(self):
        #dessine un cercle
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon,
                                  self.color)
        self.mouvement()

class rectangle(Forme):
    def draw(self):
        #dessine un rectangle
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.height,self.width,
                                  self.color,self.angle,)
        self.mouvement()
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "")
        #crée la liste forme
        self.liste_formes = []

    def on_draw(self):
        arcade.start_render()

        for forme in self.liste_formes:
            forme.draw()


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

            if button == arcade.MOUSE_BUTTON_LEFT:
                # taille
                rayon = random.randint(15, 45)
                # emplacement
                center_x= x
                center_y= y

                # vitesse
                m_x = random.randint(3, 6)
                m_y = random.randint(3, 6)

                # couleur
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                alpha = random.randint(50, 255)
                color = (red, green, blue, alpha)
                Cercle = cercle(rayon, center_x, center_y, color, m_x, m_y)
                self.liste_formes.append(Cercle)


            if button == arcade.MOUSE_BUTTON_RIGHT:

                # taille
                width = random.randint(15, 45)
                height = random.randint(15, 45)

                # angle
                angle = random.randint(0, 360)

                # emplacement
                center_x = x
                center_y = y

                # vitesse
                m_x = random.randint(0, 10)
                m_y = random.randint(0, 10)

                # couleur
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                alpha = random.randint(50, 255)
                color = (red, green, blue, alpha)
                Rectangle = rectangle(height, width, center_x, center_y, color, m_x, m_y, angle)
                self.liste_formes.append(Rectangle)


def main():
    my_game = MyGame()
    arcade.run()


main()
