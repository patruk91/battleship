import os


def main():
    board_print(board_create())
    index = handle_ship_indexes(handle_ship_position())
    size = ship_size()
    while True:
        shoot = handle_shoot()
        grid = update_board(shoot)
        board_print(grid[0])
        index = update_ship_index(grid[1], index)
        game_win = win_condition(index, size)

        if game_win is True:
            break

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
        grid, shoot = update_board(handle_shoot())
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


def ship_size():
    size = {
        "Carrier": 5,
        # "Battleship": 4,
        # "Cruiser": 3,
        # "Submarine": 3,
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
                if position[0] in numbers_of_alphabet.values() and 0 <= int(position[1]) < 10:

                    direction = handle_correct_direction()
                    correct_position = test_position(key, value, grid_for_ship, position, direction)

                    handle_grid_position(value, grid_for_ship, correct_position, direction)
                    board_print(grid_for_ship)
                    break
                else:
                    print("The ship will be outside the board!\n"
                          "Please provide a correct value!\n")
                    continue
            except IndexError:
                print("The ship will be outside the board!\n"
                      "Please provide a correct value!\n")

    return grid_for_ship


def test_position(key, value, grid_for_ship, position, direction):
    value_copy = value

    while True:
        ship_in_grid = []
        value = value_copy - 1
        while value >= 0:
            if direction == "h":
                if grid_for_ship[position[1]][position[0] + value] == "S":
                    print("I can't place ship here! It's colliding with another!\n")
                    value -= 1
                    ship_in_grid.append(True)

                else:
                    value -= 1
                    ship_in_grid.append(False)

            elif direction == "v":
                if grid_for_ship[position[1] + value][position[0]] == "S":
                    print("I can't place ship here! It's colliding with another!\n")
                    value -= 1
                    ship_in_grid.append(True)

                else:
                    value -= 1
                    ship_in_grid.append(False)

        if True in ship_in_grid:
            ship_place = input("Where you want place the {} (e.g A1 or 1A): ".format(key))
            position = handle_user_coordinates(ship_place)
        else:
            return position


def handle_grid_position(value, grid_for_ship, position, direction):
    value -= 1  # due to counting in list
    while value >= 0:
        if direction == "h":
            grid_for_ship[position[1]][position[0] + value] = "S"
            value -= 1
        elif direction == "v":
            grid_for_ship[position[1] + value][position[0]] = "S"
            value -= 1
    handle_ship_indexes(grid_for_ship)
    return grid_for_ship


def handle_correct_direction():
    direction = input("Do you want to put the ship vertically (v) or horizontally? (h): ")
    while True:
        if direction == "v" or direction == "h":
            return direction
        else:
            print("\nDirection value need to be: 'v' or 'h'!")
            direction = input("Do you want to put the ship vertically (v) or horizontally? (h): ")


def handle_ship_indexes(grid_for_ship):
    size = list(ship_size().values())
    ship_indexes = []

    for index1, value1 in enumerate(grid_for_ship):
        for index2, value2 in enumerate(value1):
            if value2 == 'S':
                res = (index1, index2)
                ship_indexes.append(res)

    ship_indexes = [ship_indexes[sum(size[:i]):sum(size[:i+1])] for i in range(len(size))]
    return ship_indexes


def update_ship_index(shoot, ship_index):
    ship_index = [[True if i == tuple(shoot[::-1]) else i for i in value] for value in ship_index]
    display_info_about_destroy_ship(ship_index)
    return ship_index


def display_info_about_destroy_ship(ship_index):
    size = ship_size()
    i = 0
    while i < len(ship_index):
        if len(set(ship_index[i])) == 1:
            for key, value in size.items():
                if len(ship_index[i]) == value:
                    print("YOU ANNIHILATE {}!" .format(key.upper()))
            ship_index[i] = []
            break
        i += 1

def win_condition(ship_index, size):
    i = 0
    while i < len(ship_index):
        if ship_index == [[]] * len(size):
            print("YOU WON!")
            i += 1
            return True
        else:
            i += 1
            return False



def handle_shoot():
    numbers_of_alphabet = handle_alphabet()

    while True:
        coordinates = input("Please, give me a position where you want to shoot (e.g A1 or 1A): ").lower()
        shoot = handle_user_coordinates(coordinates)
        if shoot[0] in numbers_of_alphabet.values() and 0 <= int(shoot[1]) < 10:
            break

    return shoot


def handle_user_coordinates(coordinates):
    numbers_of_alphabet = handle_alphabet()
    try:
        user_character = "".join([number for number in coordinates if not number.isdigit()])
        user_number = "".join([number for number in coordinates if number.isdigit()])
        coordinates = [numbers_of_alphabet.get(user_character)] + [int(user_number) - 1]
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


if __name__ == "__main__":
    main()
