import models.user as us


def get_leaderboard(user_list: list):
    i: us.User
    leaderboard = []
    for i in user_list:
        leaderboard.append((i.get_username(), i.get_games_played(), i.get_wins()))
    leaderboard.sort(key=sort_by_win, reverse=True)
    return leaderboard


def sort_by_win(elem):
    return elem[2]


def new_game(player2, user_list):
    user_found = False
    for i in user_list:
        if i.get_username() == player2:
            user_found = True
    if user_found is False:
        return "User not found."
    else:
        play_grid = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
        return play_grid


def check_win_condition(play_grid, player):
    # Check rows
    for row in play_grid:
        for i in range(len(row) - 3):
            if row[i:i + 4] == [player] * 4:
                return True

    # Check columns
    for col in range(len(play_grid[0])):
        for i in range(len(play_grid) - 3):
            if [row[col] for row in play_grid[i:i + 4]] == [player] * 4:
                return True

    # Check diagonals
    for row in range(len(play_grid) - 3):
        for col in range(len(play_grid[0]) - 3):
            if [play_grid[row + i][col + i] for i in range(4)] == [player] * 4:
                return True
            if [play_grid[row + 3 - i][col + i] for i in range(4)] == [player] * 4:
                return True
    return False


def insert_piece1(grid, column_id):
    for row in range(len(grid) - 1, -1, -1):
        if grid[row][column_id] == 0:
            grid[row][column_id] = 1
            if check_win_condition(grid, 1):
                return grid, True
            return grid, False
    return grid, False


def insert_piece2(grid, column_id):
    for row in range(len(grid) - 1, -1, -1):
        if grid[row][column_id] == 0:
            grid[row][column_id] = 2
            if check_win_condition(grid, 2):
                return grid, True
            return grid, False
    return grid, False
