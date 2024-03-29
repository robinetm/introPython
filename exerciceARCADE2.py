#crée le mathis robinet
#crée par 2023/03/20
#exercice arcade 2


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_SHAPES = 20

class Cercle():
    def __init__(self, r,x,y,c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)

    def draw(self):
        #arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []



    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(NUMBER_OF_SHAPES):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            red= random.randint(0,255)
            green= random.randint(0,255)
            blue= random.randint(0,255)
            alpha = random.randint(0, 255)
            color=(red,green,blue,alpha)
            cercle= Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            if x < cercle.centre_x + cercle.rayon and x > cercle.centre_x - cercle.rayon and y < cercle.centre_y + cercle.rayon and \
                    y > cercle.centre_y - cercle.rayon:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.liste_cercles.remove(cercle)

                if button == arcade.MOUSE_BUTTON_RIGHT:
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    alpha = random.randint(0, 255)
                    color = (red, green, blue, alpha)
                    cercle.color= color





def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
