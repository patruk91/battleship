import board_map as bm
import shoot_system as ss


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
    numbers_of_alphabet = ss.handle_alphabet()
    grid_for_ship = bm.board_create()

    for key, value in size.items():
        while True:
            ship_place = input("Where you want place the {} (e.g A1 or 1A): ".format(key))
            position = ss.handle_user_coordinates(ship_place)
            try:
                if position[0] in numbers_of_alphabet.values() and 0 <= int(position[1]) < 10:

                    direction = handle_correct_direction()
                    correct_position = test_position(key, value, grid_for_ship, position, direction)

                    handle_grid_position(value, grid_for_ship, correct_position, direction)
                    bm.board_print(grid_for_ship)
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
            position = ss.handle_user_coordinates(ship_place)
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
