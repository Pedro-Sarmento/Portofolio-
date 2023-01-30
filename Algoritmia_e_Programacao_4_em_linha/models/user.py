class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.wins = 0
        self.games_played = 0

    def get_wins(self):
        return self.wins

    def get_games_played(self):
        return self.games_played

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def add_win(self):
        self.wins += 1

    def add_game_played(self):
        self.games_played += 1
