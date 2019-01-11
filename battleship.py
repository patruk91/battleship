import ship
import board_map as bm
import shoot_system as ss
import os


def main():
    bm.board_print(bm.board_create())
    index = ship.handle_ship_indexes(ship.handle_ship_position())
    size = ship.ship_size()

    while True:
        shoot = ss.handle_shoot()
        grid = bm.update_board(shoot)
        bm.board_print(grid[0])
        index = ship.update_ship_index(grid[1], index)
        game_win = ship.win_condition(index, size)

        if game_win is True:
            break


if __name__ == "__main__":
    main()
