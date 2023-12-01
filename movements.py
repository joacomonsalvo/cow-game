from mold import coordinates


def go_right(mold, gates, arrived, score, difficulty):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if c == 4:
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
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

    return mold, gates, arrived, score, next_position, difficulty


def go_up(mold, gates, arrived, score, difficulty):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if r == 0:
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        r = 4
        next_position = mold[r][c]
        score -= 10

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

        mold[r][c] = "&"

    else:
        next_position = mold[r - 1][c]
        score -= 10
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        mold[r - 1][c] = "&"

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

    return mold, gates, arrived, score, next_position, difficulty


def go_down(mold, gates, arrived, score, difficulty):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if r == 4:
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        r = 0
        mold[r][c] = "&"
        next_position = mold[r][c]
        score -= 10

    else:
        next_position = mold[r + 1][c]
        score -= 10
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        mold[r + 1][c] = "&"

    if next_position == "T":
        gates += 1
        score -= 25
    elif next_position == "E" and gates == n_gates:
        arrived = True
        score += 500
    elif next_position == "P":
        score += 250

    return mold, gates, arrived, score, next_position, difficulty


def go_left(mold, gates, arrived, score, difficulty):
    r, c = coordinates(mold)
    n_gates = 2 * difficulty + 5

    if c == 0:
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        c = 4
        next_position = mold[r][c]
        score -= 10

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

        mold[r][c] = "&"

    else:
        next_position = mold[r][c - 1]
        score -= 10
        mold[r][c] = "I" if mold[r][c] != "E" else "E"
        mold[r][c - 1] = "&"

        if next_position == "T":
            gates += 1
            score -= 25
        elif next_position == "E" and gates == n_gates:
            arrived = True
            score += 500
        elif next_position == "P":
            score += 250

    return mold, gates, arrived, score, next_position, difficulty
