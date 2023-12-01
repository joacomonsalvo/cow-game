from colorama import Fore as c_fore
from colorama import Style as c_style
import colorama
import random


def create_mold(difficulty):
    cow = "&"
    grass = "I"
    food = "P"
    gate = "T"
    barn = "E"

    mold = [["0"] * 5 for _ in range(5)]

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
            row = random.randint(0, len(mold) - 1)
            column = random.randint(0, len(mold) - 1)
            if mold[row][column] == "0":
                mold[row][column] = item_type
                break

    return mold


def print_map(mold):
    colorama.init()

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


def reset(message, score_value, difficulty_value, gates_value, arrived_value):
    print(message)
    score = score_value
    difficulty = difficulty_value
    gates = gates_value
    mold = create_mold(difficulty)
    arrived = arrived_value

    return score, difficulty, gates, mold, arrived
