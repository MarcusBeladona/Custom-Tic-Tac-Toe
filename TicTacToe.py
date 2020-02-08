import os
import time


def ai_move(board):

    table = ([board[0], board[1], board[2]],
             [board[3], board[4], board[5]],
             [board[6], board[7], board[8]],

             [board[0], board[3], board[6]],
             [board[1], board[4], board[7]],
             [board[2], board[5], board[8]],

             [board[0], board[4], board[8]],
             [board[2], board[4], board[6]],)

    positions = ([0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],

                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],

                 [0, 4, 8],
                 [2, 4, 6],)

    chances = ([" ", humano, humano],
               [humano, " ", humano],
               [humano, humano, " "])

    for index, i in enumerate(table):
        if i in chances:
            for k in range(3):
                if i == chances[k]:
                    pos = positions[index]
                    return pos[k]

    else:
        return minimax(posicoes, len(empty_cells(posicoes)), player)[0]


def win(board, player):

    # CUIDADO! VOCÊ VAI SE CONFUNDIR.

    for i in ("X", "O"):

        if [i, i, i] in ([board[0], board[1], board[2]],
                         [board[3], board[4], board[5]],
                         [board[6], board[7], board[8]],

                         [board[0], board[3], board[6]],
                         [board[1], board[4], board[7]],
                         [board[2], board[5], board[8]],

                         [board[0], board[4], board[8]],
                         [board[2], board[4], board[6]],):

            if i == player:
                return 1
            else:
                return -1
    else:
        if len(empty_cells(board)) == 0:
            return 0
        else:
            return "null"


def minimax(state, depth, player):

    if depth == 0 or end_game(state):
        result = win(state, player_switch(player))
        if result == 1:
            nodos = 1
        else:
            nodos = 0
        return "null", result, nodos

    score = []
    cells = empty_cells(state)
    chances = []
    nodos = 0

    for i in cells:
        state[i] = player
        best, aux, chance = minimax(state, depth-1, player_switch(player))
        score.append(aux)
        chances.append(chance)
        state[i] = " "

    for k in chances:
        nodos += k

    melhor_nodo = min(chances)

    if player == computer:

        result = max(score)

        for j in range(len(score)):
            if score[j] == result and chances[j] == melhor_nodo:
                best = cells[j]
                break

    elif player == humano:

        result = min(score)

        for j in range(len(score)):
            if score[j] == result:
                best = cells[j]
                break

    return best, result, nodos


def make_move(board, index, player):
    if valid_move(board, index):
        board[index] = player
        return True
    else:
        return False


def valid_move(board, index):
    return True if board[index] == " " else False


def empty_cells(board):
    cells = []
    for i in range(0, 9):
        if board[i] == " ":
            cells.append(i)
    return cells


def end_game(board):
    if (win(board, humano) or win(board, computer)) == 1:
        return True
    else:
        return False


def evaluate(board):
    if win(board, computer):
        return +1
    elif win(board, humano):
        return -1
    else:
        return 0


def player_switch(player):
    return "X" if player == "O" else "O"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_tabuleiro(posicoes):
    print("-------------")
    print(f"| {posicoes[0]} | {posicoes[1]} | {posicoes[2]} |")
    print("-------------")
    print(f"| {posicoes[3]} | {posicoes[4]} | {posicoes[5]} |",)
    print("-------------")
    print(f"| {posicoes[6]} | {posicoes[7]} | {posicoes[8]} |",)
    print("-------------")


def game_status():

    status = win(posicoes, humano)

    if status == 1:  # Ganhou
        clear_console()
        print_tabuleiro(posicoes)
        print("Você ganhou!")
        time.sleep(1)
        return True

    elif status == -1:  # Perdeu
        clear_console()
        print_tabuleiro(posicoes)
        print("Você perdeu!")
        time.sleep(1)
        return True

    elif status == 0:  # Empate
        clear_console()
        print_tabuleiro(posicoes)
        print("Empate!")
        time.sleep(1)
        return True

    else:
        return False


while True:

    posicoes = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    clear_console()
    print("--------------")
    print("TIC! TAC! TOE!")
    print("--------------")
    print()
    humano = input("Com quem você vai jogar? X ou O: ").capitalize()

    if humano in ("X", "O"):

        computer = "X" if humano == "O" else "O"
        clear_console()
        print("Estas são as posições do tabuleiro:")
        print_tabuleiro([1, 2, 3, 4, 5, 6, 7, 8, 9])
        input("Aperte qualquer tecla para continuar...")

        player = humano

        while True:
            clear_console()

            if game_status():
                break

            if player == humano:
                print("Sua vez:")
                print_tabuleiro(posicoes)

                try:
                    posicao = int(input("Digite uma posição para jogar: "))
                    if posicao in range(1, 10):
                        if make_move(posicoes, posicao-1, humano):
                            player = player_switch(player)
                        else:
                            print("Posição ocupada.")
                            time.sleep(1)
                    else:
                        print("Número inválido.")
                        time.sleep(1)
                except Exception as e:
                    print("Opção inválida.")
                    time.sleep(1)

            else:
                print("Vez da I.A:")
                print_tabuleiro(posicoes)

                posicao = ai_move(posicoes)

                make_move(posicoes, posicao, computer)
                player = player_switch(player)

    else:
        print("Opção inválida.")
        time.sleep(1)
