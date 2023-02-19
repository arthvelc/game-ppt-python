import os


def game_instructions():
    print("""\tInstrucciones del juego
    selecciona la opción con la cual vas a atacar :
    1. ==> Piedra 🪨
    2. ==> Papel 🧻
    3. ==> Tijeras ✂️
    """)

    input('¡Listo! presiona ---ENTER--- para comenzar 😎 ')


def num_partidas():
    while True:
        try:
            rounds = int(input("¿Cuántas partidas quieres jugar? "))
        except NameError:
            print("Digita el número de rounds con un numero entero positivo")
        except ValueError:
            print("Digita el numero con un entero positivo")
        else:
            False
            return rounds


def star_game():
    print(""""¡¡¡¡¡¡¡¡¡¡COMIENZA EL JUEGO!!!!!!!!!!!!!!""")


def rounds_count(numero_partidas=1):
    print(f"""*************
ROUND {numero_partidas}
*************""")


def pause():
    input("Presiona enter para continuar")


def contador_resultados(victorias, derrotas, empates, rounds):
    print(f"""Resultados de la contienda:

De {rounds} partidas...

El numero de victorias fue de: {victorias}
El número de derrotas fue de: {derrotas}
El número de empates fue de: {empates}""")


def end():
    print("Gracias por haber jugado el mítico juego de piedra papel o tijeras")


def clear():
    os.system('clear')
