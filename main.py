import random
import colorama
from colorama import Fore as c_fore
from colorama import Style as c_style

colorama.init()

score = 100
difficulty = 1
gates = 0
mold = []
arrived = False
next_position = 0


def create_map(mold, difficulty):
    cow = "&"
    grass = "I"
    food = "P"
    gate = "T"
    barn = "E"

    mold = [[0 for zero in range(5)] for zeros in range(5)]
    mold[0][0] = cow
    mold[4][4] = barn

    n_gates = [7, 9, 11]
    n_grass = [8, 7, 6]
    n_food = [8, 7, 6]

    mold = random_gen(mold, n_gates, gate, difficulty)
    mold = random_gen(mold, n_grass, grass, difficulty)
    mold = random_gen(mold, n_food, food, difficulty)

    return mold


def random_gen(mold, number_items, item_type, difficulty):
    for item in range(number_items[difficulty - 1]):
        while True:
            row = random.randint(0, 4)
            column = random.randint(0, 4)
            if mold[row][column] == 0:
                mold[row][column] = item_type
                break

    return mold


def print_map(mold):
    for row in mold:
        for column in row:
            if column == "&":
                print(f"{c_fore.RED}{column}	{c_style.RESET_ALL}", end="")
            elif column == "P":
                print(f"{c_fore.LIGHTGREEN_EX}{column}	{c_style.RESET_ALL}", end="")
            elif column == "T":
                print(f"{c_fore.WHITE}{column}	{c_style.RESET_ALL}", end="")
            elif column == "I":
                print(f"{c_fore.GREEN}{column}	{c_style.RESET_ALL}", end="")
            elif column == "E":
                print(f"{c_fore.LIGHTCYAN_EX}{column}	{c_style.RESET_ALL}", end="")
            else:
                print(f"{c_fore.CYAN}{column}	{c_style.RESET_ALL}", end="")
        print()


def coordinates(mold):
    for r in range(len(mold)):
        for c in range(len(mold[r])):
            if mold[r][c] == "&":
                return r, c


def go_right(mold, gates, arrived, score, next_position):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if c == 4:
        mold[r][c] = "I"
        c = 0
        mold[r][c] = "&"
        next_position = mold[r][c]
        score -= 10

    else:
        next_position = mold[r][c + 1]
        score -= 10
        mold[r][c] = "I"
        mold[r][c + 1] = "&"

    if next_position == "T":
        gates += 1
        score -= 25
    elif next_position == "E" and gates == n_gates:
        arrived = True
        score += 500
    elif next_position == "P":
        score += 250

    return mold, gates, arrived, score, next_position


def go_up(mold, gates, arrived, score, next_position):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if r == 0:
        mold[r][c] = "I"
        r = 4
        next_position = mold[r][c]
        score -= 10

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "E" and gates != n_gates:
            next_position = 'E'
        elif next_position == "P":
            score += 250

        mold[r][c] = "&"

    else:
        next_position = mold[r - 1][c]
        score -= 10
        mold[r][c] = "I"
        mold[r - 1][c] = "&"

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

    return mold, gates, arrived, score, next_position


def go_down(mold, gates, arrived, score, next_position):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if r == 4:
        mold[r][c] = "I"
        r = 0
        mold[r][c] = "&"
        next_position = mold[r][c]
        score -= 10

    else:
        next_position = mold[r + 1][c]
        score -= 10
        mold[r][c] = "I"
        mold[r + 1][c] = "&"

    if next_position == "T":
        gates += 1
        score -= 25
    elif next_position == "E" and gates == n_gates:
        arrived = True
        score += 500
    elif next_position == "P":
        score += 250

    return mold, gates, arrived, score, next_position


def go_left(mold, gates, arrived, score, next_position):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if c == 0:
        mold[r][c] = "I"
        c = 4
        next_position = mold[r][c]
        score -= 10

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "E" and gates != n_gates:
            next_position = 'E'
        elif next_position == "P":
            score += 250

        mold[r][c] = "&"

    else:
        next_position = mold[r][c - 1]
        score -= 10
        mold[r][c] = "I"
        mold[r][c - 1] = "&"

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

    return mold, gates, arrived, score, next_position


if __name__ == "__main__":
    mold = create_map(mold, difficulty)

    while not arrived and score > 0:
        print(f"{c_fore.BLUE} Level: {difficulty} {c_style.RESET_ALL}")
        print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
        print(f"{c_fore.YELLOW} Gates: {gates} {c_style.RESET_ALL}")
        print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
        print()

        print_map(mold)
        cursor = input("->")
        if cursor.upper() == "W":
            mold, gates, arrived, score, next_position = go_up(mold, gates, arrived, score, next_position)
        elif cursor.upper() == "D":
            mold, gates, arrived, score, next_position = go_right(mold, gates, arrived, score, next_position)
        elif cursor.upper() == "S":
            mold, gates, arrived, score, next_position = go_down(mold, gates, arrived, score, next_position)
        elif cursor.upper() == "A":
            mold, gates, arrived, score, next_position = go_left(mold, gates, arrived, score, next_position)

        if arrived:
            print(f"{c_fore.BLUE} Level: {difficulty} {c_style.RESET_ALL}")
            print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
            print(f"{c_fore.YELLOW} Gates: {gates} {c_style.RESET_ALL}")
            print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
            print()
            print_map(mold)

            if difficulty < 3:
                print("LEVEL COMPLETED!")
                score = 100
                difficulty = difficulty + 1
                gates = 0
                mold = create_map(mold, difficulty)
                arrived = False
                continue

            else:
                print("YOU WIN")
                play_again = input("\nDo you want to play again? YES or NO ").upper()

                if play_again == "YES":
                    score = 100
                    difficulty = 1
                    gates = 0
                    mold = create_map(mold, difficulty)
                    arrived = False
                    continue

                elif play_again == "NO":
                    break

        elif score <= 0:
            print("GAME OVER")
            play_again = input("\nDo you want to play again? YES or NO ").upper()

            if play_again == "YES":
                score = 100
                difficulty = 1
                gates = 0
                mold = create_map(mold, difficulty)
                arrived = False
                continue

            elif play_again == "NO":
                break

        elif next_position == "E" and gates != 7:
            print("GAME OVER, Invalid Movement")
            play_again = input("\nDo you want to play again? YES or NO ").upper()

            if play_again == "YES":
                score = 100
                difficulty = 1
                gates = 0
                mold = create_map(mold, difficulty)
                arrived = False
                continue

            elif play_again == "NO":
                break
