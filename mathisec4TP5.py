import arcade
import random
from enum import Enum

number_to_text = {
0: &quot;zéro&quot;,
1: &quot;un&quot;,
2: &quot;deux&quot;,
3: &quot;trois&quot;,
4: &quot;quatre&quot;
}
for i in range(5):
print(number_to_text[i], end=&quot; &quot;)


class GameState(Enum):
NOT_STARTED = 0

if self.player_attack_type[AttackType.ROCK]:
pass

if self.game_state == GameState.RenderInventory:
# Dessiner la fenêtre de l&#39;inventaire
pass
elif self.game_state == GameState.RenderMenu:
# Dessiner le menu principal
pass

coin = arcade.Sprite(&quot;:resources:images/items/coinGold.png&quot;, SPRITE_SCALING_COIN)

coin.center_x = 200
coin.center_y = 200
coin.draw()

def on_mouse_press(self, x, y, button, key_modifiers):
if self.hero.collides_with_point((x, y)):
print(&quot;L&#39;usager a cliqué sur le héros.&quot;)

self.coin_list = arcade.SpriteList()

for i in range(10):
coin = arcade.Sprite(&quot;:resources:images/items/coinGold.png&quot;)
self.coin_list.append(coin)

self.coin_list.draw()

class AttackType(Enum):
&quot;&quot;&quot;
Simple énumération pour représenter les différents types d&#39;attaques.
&quot;&quot;&quot;
ROCK = 0,
PAPER = 1,
SCISSORS = 2

class AttackAnimation(arcade.Sprite):
ATTACK_SCALE = 0.50
ANIMATION_SPEED = 5.0
