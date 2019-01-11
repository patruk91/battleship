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
