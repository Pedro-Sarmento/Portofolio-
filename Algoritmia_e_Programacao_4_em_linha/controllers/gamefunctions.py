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

