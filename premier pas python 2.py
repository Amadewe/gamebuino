from gamebuino_meta import begin, waitForUpdate, display, buttons, color

while True:
    waitForUpdate()
    display.clear()

    name = "Brian"
    score = 15
    lives = 3

    display.setColor(color.BLUE)
    display.print(name)

    display.setColor(color.GREEN)
    display.print(" (vies : ")
    display.setColor(color.RED)
    display.print(lives)
    display.setColor(color.GREEN)
    display.print(")")

    display.print("\n")
    display.print("\n")

    display.setColor(color.WHITE)
    display.print("Score : ")
    display.print(score)

    display.print("\n")
    display.print("\n")

    lives = 2

    display.print("J'ai perdu une vie !")

    display.print("\n")
    display.print("\n")

    display.setColor(color.GREEN)
    display.print("Vies restantes : ")
    display.setColor(color.RED)
    display.print(lives)