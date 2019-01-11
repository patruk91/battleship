import shoot_system as ss


def update_board(shoot):
    grid = board_create()
    if grid[shoot[1]][shoot[0]] == "S":
        # os.system('clear')
        grid[shoot[1]][shoot[0]] = "#"
        print("YOU HAVE A HIT!")

    elif grid[shoot[1]][shoot[0]] == "~":
        # os.system('clear')
        grid[shoot[1]][shoot[0]] = "&"
        print("YOU MISS!")

    else:
        # os.system('clear')
        print("YOU ALREADY SHOOT HERE!")
        grid, shoot = update_board(ss.handle_shoot())
        return grid, shoot

    return grid, shoot


def board_create(grid=[]):
    if grid == []:
        for num in range(10):
            grid.append(["~"] * 10)
    return grid


def board_print(grid):
    alphabet = list(map(chr, range(65, 75)))
    print("    " + "   ".join(alphabet))

    return handle_format_line_in_board(grid)


def handle_format_line_in_board(grid):
    line = "  "
    i = 1
    line += "-" * 41 + "\n"
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
    print(line)
