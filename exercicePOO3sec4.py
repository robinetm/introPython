import arcade


class MyGame(arcade.Window):
   def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

def main():

    window = MyGame(640, 480, "Drawing Example")
    arcade.run()

def on_draw(self):
   """
   C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
   de votre jeu à l'écran.
   """

   arcade.start_render()

   arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))


main()
