# In this module, I pay the game logic functions
import random
import showscreen as show


def pc_option():
    return random.randrange(1, 4)


def game(count, rounds):
    victories = 0
    defeated = 0
    empate = 0
    while count <= rounds:
        show.rounds_count(count)

        while True:
            try:
                # Seleccioon de la optión del jugador
                userOption = int(input('Elige tu arma ==> '))
            except NameError:
                print("Digite un opción valida con un número entero.")
            except ValueError:
                print("Digite un opción valida con un número entero.")
            else:
                break

        # Selección de armas
        if userOption == 1:
            print("""Elegiste Piedra 🪨""")
        elif userOption == 2:
            print("""Elegiste Papel 🧻""")
        elif userOption == 3:
            print("""Elegiste tijeras ✂️""")

        computerOption = pc_option()
        if computerOption == 1:
            print("""La Computadora Eligió Piedra 🪨""")
        elif computerOption == 2:
            print("""La computadora Eligió Papel 🧻""")
        elif computerOption == 3:
            print("""La computadora eligió Tijeras ✂️""")

        # Aquí irá la regla del juego, quien gana y quien pierde.

        if computerOption == userOption:
            print("Empate")
            empate += 1
        else:
            if computerOption == 1 and userOption == 2:
                print("Ganaste")
                victories += 1
            elif computerOption == 1 and userOption == 3:
                print("Perdiste")
                defeated += 1
            elif computerOption == 2 and userOption == 1:
                print("perdiste")
                defeated += 1
            elif computerOption == 2 and userOption == 3:
                print("Ganaste")
                victories += 1
            elif computerOption == 3 and userOption == 1:
                print("perdiste")
                defeated += 1
            else:
                print("Ganaste")
                victories += 1
        count += 1
        show.pause()
        show.clear()

    return victories, defeated, empate
