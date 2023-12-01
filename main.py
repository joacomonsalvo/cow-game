from movements import go_up, go_down, go_left, go_right
from colorama import Fore as c_fore
from colorama import Style as c_style
from mold import create_mold, print_map, reset
import colorama


if __name__ == "__main__":
    colorama.init()

    score = 100
    difficulty = 1
    gates = 0
    arrived = False
    next_position = 0

    mold = create_mold(difficulty)

    while not arrived and score > 0:
        print(f"{c_fore.BLUE} Level: {difficulty} {c_style.RESET_ALL}")
        print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
        print(f"{c_fore.YELLOW} Gates: {gates} {c_style.RESET_ALL}")
        print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
        print()

        print_map(mold)
        cursor = input("->")
        if cursor.upper() == "W":
            mold, gates, arrived, score, next_position, difficulty = go_up(mold, gates, arrived, score, difficulty)
        elif cursor.upper() == "D":
            mold, gates, arrived, score, next_position, difficulty = go_right(mold, gates, arrived, score, difficulty)
        elif cursor.upper() == "S":
            mold, gates, arrived, score, next_position, difficulty = go_down(mold, gates, arrived, score, difficulty)
        elif cursor.upper() == "A":
            mold, gates, arrived, score, next_position, difficulty = go_left(mold, gates, arrived, score, difficulty)

        if arrived:
            print(f"{c_fore.BLUE} Level: {difficulty} {c_style.RESET_ALL}")
            print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
            print(f"{c_fore.YELLOW} Gates: {gates} {c_style.RESET_ALL}")
            print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
            print()
            print_map(mold)

            if difficulty < 3:
                reset("LEVEL COMPLETED!", 100, difficulty + 1, 0, False)

            else:
                print("YOU WIN")
                play_again = input("\nDo you want to play again? YES or NO ").upper()

                if play_again == "YES":
                    reset("", 100, 1, 0, False)

                elif play_again == "NO":
                    break

        elif score <= 0:
            print("GAME OVER")
            play_again = input("\nDo you want to play again? YES or NO ").upper()

            if play_again == "YES":
                reset("", 100, 1, 0, False)

            elif play_again == "NO":
                break

        elif next_position == "E" and gates != 7:
            print("GAME OVER, Invalid Movement")
            play_again = input("\nDo you want to play again? YES or NO ").upper()

            if play_again == "YES":
                reset("", 100, 1, 0, False)

            elif play_again == "NO":
                break
