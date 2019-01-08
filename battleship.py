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


def ship_size():
    size = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }
    return size


def handle_ship_position():
    size = ship_size()
    numbers_of_alphabet = handle_alphabet()
    grid_for_ship = board_create()

    for key, value in size.items():
        while True:
            ship_place = input("Where you want place the {} (e.g A1 or 1A): ".format(key))
            position = handle_user_coordinates(ship_place)
            try:
                if position[0] in numbers_of_alphabet.values() and 0 < int(position[1]) < 11:
                    direction = input("Do you want to put the ship vertically (v) or horizontally? (h)")

                    if direction == "h":
                        correct_position = test_position(key, value, grid_for_ship, position)
                        handle_horizontal_position(value, grid_for_ship, correct_position)

                    elif direction == "v":
                        handle_vertical_position(value, grid_for_ship, position)

                    board_print(grid_for_ship)
                    break
                else:
                    continue
            except IndexError:
                print("Please provide a correct value!\n")

    return grid_for_ship


def test_position(key, value, grid_for_ship, position):
    cp = value


    while True:
        listaa = []
        value = cp
        while value > 0:
            if grid_for_ship[position[1] - 1][position[0] + value - 1] == "S":
                print("I can't place ship here! It's colliding with another!\n")
                value -= 1
                x = False
                listaa.append(x)

            else:
                value -= 1
                x = True
                listaa.append(x)

        if False in listaa:
            ship_place = input("Where you want place the {} (e.g A1 or 1A): ".format(key))
            position = handle_user_coordinates(ship_place)
        else:
            return position


def handle_horizontal_position(value, grid_for_ship, position):
    while value > 0:
        grid_for_ship[position[1] - 1][position[0] + value - 1] = "S"
        value -= 1
    return grid_for_ship


def handle_vertical_position(value, grid_for_ship, position):
    while value > 0:
        grid_for_ship[position[1] + value - 2][position[0]] = "S"
        value -= 1
    return grid_for_ship


def handle_shoot():
    numbers_of_alphabet = handle_alphabet()

    while True:
        coordinates = input("Please, give me a position where you want to shoot (e.g A1 or 1A): ").lower()
        shoot = handle_user_coordinates(coordinates)
        if shoot[0] in numbers_of_alphabet.values() and 0 < int(shoot[1]) < 11:
            break

    return shoot


def handle_user_coordinates(coordinates):
    numbers_of_alphabet = handle_alphabet()
    try:
        user_character = "".join([number for number in coordinates if not number.isdigit()])
        user_number = "".join([number for number in coordinates if number.isdigit()])
        coordinates = [numbers_of_alphabet.get(user_character)] + [int(user_number)]
    except ValueError:
        print("", end="")

    return coordinates


def handle_alphabet():
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
    return numbers_of_alphabet


print(handle_ship_position())
if __name__ == "__main__":
    main()
