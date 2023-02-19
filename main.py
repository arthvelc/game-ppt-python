# mítico juego de piedra papel o tijeras
# vamos a empezar a programar de verdad
# jaja rompí el código, pero luego lo arreglo, mientras este código servirá para fines prácticos 20/dic/2022.
# Ya estructuré  mejor el programa modularizando procesos en el algoritmo :D  29/12/22
# Me encanta prpogramar, incorporé el bucle while en la funcioón game y corregí el contador de resultados y puse algunos manejos de error, voy a continuar mejorando ya que talta poner un límite en las opciones:D 2/01/2023

import showscreen as show
import game_rules as game


def run():
    show.clear()
    show.game_instructions()
    show.clear()
    rounds = show.num_partidas()
    show.clear()
    show.star_game()
    victorias, derrotas,  empates = game.game(count=1, rounds=rounds)
    show.contador_resultados(victorias, derrotas, empates, rounds)
    show.pause()
    show.clear()
    show.end()


if __name__ == '__main__':
    run()
