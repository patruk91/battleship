def main():
    board_print(board_create())
    while True:
        shoot = handle_shoot()
        grid = update_board(shoot)
        board_print(grid)





def update_board(shoot):
    grid = board_create()
    grid[shoot[1] - 1][shoot[0]] = "#"
    return grid


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



def handle_shoot():
    numbers_of_alphabet = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
    }


    while True:
        shoot = input("Please, give me a position where you want to shoot (e.g A1): ").lower()
        shoot_char = "".join([number for number in shoot if not number.isdigit()])
        shoot_num = "".join([number for number in shoot if number.isdigit()])
        shoot = [numbers_of_alphabet.get(shoot_char)] + [int(shoot_num)]

        if shoot_char in numbers_of_alphabet and 0 < int(shoot_num) < 11:
            break
    return shoot





# grid[numbers_of_alphabet.get(shoot_char)][int(shoot_num) - 1] = "#"

    # try:
    #     grid_1 = int(numbers_of_alphabet[shoot[0]])
    #     grid_2 = int(shoot[1]) - 1  # we start count the table from one
    #     print('git')
    # except KeyError:
    #     print('wrong nums')




if __name__ == "__main__":
    main()
