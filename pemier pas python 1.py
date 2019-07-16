# Ecrit ton programme ici ;-)
from gamebuino_meta import begin, waitForUpdate, display, buttons, color

while True:
    waitForUpdate()
    display.clear()

    display.print("Hello world")