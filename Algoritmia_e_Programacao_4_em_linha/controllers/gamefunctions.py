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
