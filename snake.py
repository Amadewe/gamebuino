from gamebuino_meta import waitForUpdate, display, color, buttons

# ----------------------------------------------------------
# Global variables
# ----------------------------------------------------------

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 64
COLOR_BG      = 0xFB06
COLOR_WALL    = 0x6FE6

#pour le serpent

SNAKE_SIZE = 2
COLS       = (SCREEN_WIDTH  - 4) // SNAKE_SIZE
ROWS       = (SCREEN_HEIGHT - 4) // SNAKE_SIZE
OX         = (SCREEN_WIDTH  - COLS * SNAKE_SIZE) // 2
OY         = (SCREEN_HEIGHT - ROWS * SNAKE_SIZE) // 2

# ----------------------------------------------------------
# Game management
# ----------------------------------------------------------

#Syntaxe générale d'une fonction:
#def nomDeLaFonction(liste des paramètres):
#    séquence des instructions à exécuter

# fonction, qui va se charger d'ordonnancer les différentes tâches à réaliser pour la mise en œuvre du jeu.
def tick():
    draw()

# ----------------------------------------------------------
# Graphic display
# ----------------------------------------------------------

def draw():
    display.clear(COLOR_BG)
    display.setColor(COLOR_WALL)
    display.drawRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# ----------------------------------------------------------
# Main loop
# ----------------------------------------------------------

#Boucle de contrôle principale
#La structure de contrôle while True signifie littéralement tant que Vrai
while True:
    waitForUpdate()
#pour demander à notre ordonnanceur de s'exécuter à chaque itération de la boucle de contrôle principale,
#il suffira d'effectuer un appel à la fonction tick()
    tick()