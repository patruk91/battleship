def board_create():

    grid = []
    for num in range(10):
        grid.append(["~"] * 10)
    return grid


def board_print():
    grid = board_create()
    alphabet = list(map(chr, range(65, 75)))
    line = "  "
    i = 1
    line += "-" * 41 + "\n"

    print("    " + "   ".join(alphabet))
    for row in grid:
        line += str(i)
        for column in row:
            if i == 10:
                line += "{}".format("| " + column + " ")
            else:
                line += " {}".format("| " + column)
        if i == 10:
            line += "|"
        else:
            line += " |"
        line += "\n  " + "-" * 41 + "\n"


        i += 1
    return line




print(board_print())
