import customtkinter as ctk
import controllers.gamefunctions as game_fuc
import controllers.userfunctions as user_fuc
from models.user import *


class App:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root = ctk.CTk()
        self.root.geometry("750x400")
        self.users = []
        self.active_user = None
        self.home()
        self.root.mainloop()

    def home(self):
        home_frame = ctk.CTkFrame(master=self.root)
        home_frame.pack(pady=20, padx=60, fill="both", expand=True)
        login_button = ctk.CTkButton(master=home_frame, text="Login",
                                     command=lambda: [self.login_interface(), home_frame.destroy()])
        login_button.pack(pady=12, padx=10)
        register_button = ctk.CTkButton(master=home_frame, text="Register",
                                        command=lambda: [self.register_interface(), home_frame.destroy()])
        register_button.pack(pady=12, padx=10)

    def login_interface(self):
        login_frame = ctk.CTkFrame(master=self.root)
        login_frame.pack(pady=20, padx=60, fill="both", expand=True)
        login_label = ctk.CTkLabel(master=login_frame, text="Login")
        login_label.pack(pady=12, padx=10)
        login_username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username")
        login_username_entry.pack(pady=12, padx=10)
        login_password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
        login_password_entry.pack(pady=12, padx=10)
        login_submit_button = ctk.CTkButton(master=login_frame, text="Sign in", command=lambda: self.submit_login(
            login_username_entry.get(),
            login_password_entry.get(),
            login_frame))
        login_submit_button.pack(pady=12, padx=10)
        cancel_button = ctk.CTkButton(master=login_frame, text="Cancel", command=lambda: [login_frame.destroy(),
                                                                                          self.home()])
        cancel_button.pack(pady=12, padx=10)

    def submit_login(self, username, password, frame):
        if type(user_fuc.submit_login(username, password, self.users)) is str:
            label = ctk.CTkLabel(master=frame, text=user_fuc.submit_login(username, password, self.users))
            label.pack(pady=12, padx=10)
            return
        else:
            self.active_user = user_fuc.submit_login(username, password, self.users)
            frame.destroy()
            self.menu()

    def register_interface(self):
        register_frame = ctk.CTkFrame(master=self.root)
        register_frame.pack(pady=20, padx=60, fill="both", expand=True)
        register_label = ctk.CTkLabel(master=register_frame, text="Register")
        register_label.pack(pady=12, padx=10)
        register_username_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Username")
        register_username_entry.pack(pady=12, padx=10)
        register_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Password", show="*")
        register_password_entry.pack(pady=12, padx=10)
        register_repeat_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Repeat Password",
                                                      show="*")
        register_repeat_password_entry.pack(pady=12, padx=10)
        login_submit_button = ctk.CTkButton(master=register_frame, text="Sign up",
                                            command=lambda: self.submit_register(
                                                register_username_entry.get(), register_password_entry.get(),
                                                register_repeat_password_entry.get(), register_frame))

        login_submit_button.pack(pady=12, padx=10)
        cancel_button = ctk.CTkButton(master=register_frame, text="Cancel",
                                      command=lambda: [register_frame.destroy(), self.home()])
        cancel_button.pack(pady=12, padx=10)

    def submit_register(self, username, password, password_repeat, frame):
        if type(user_fuc.submit_register(username, password, password_repeat, self.users)) is str:
            label = ctk.CTkLabel(master=frame,
                                 text=user_fuc.submit_register(username, password, password_repeat, self.users))
            label.pack(pady=12, padx=10)
            return
        else:
            new_user = user_fuc.submit_register(username, password, password_repeat, self.users)
            self.users.append(new_user)
            frame.destroy()
            self.home()

    def menu(self):
        menu_frame = ctk.CTkFrame(master=self.root)
        menu_frame.pack(pady=20, padx=60, fill="both", expand=True)
        start_game_button = ctk.CTkButton(master=menu_frame, text="New Game", command=lambda: [menu_frame.destroy(),
                                                                                               self.start_game()])
        start_game_button.pack(pady=12, padx=10)
        leaderboards_button = ctk.CTkButton(master=menu_frame, text="Leaderboard",
                                            command=lambda: [menu_frame.destroy(),
                                                             self.show_leaderboard()])
        leaderboards_button.pack(pady=12, padx=10)
        logout_button = ctk.CTkButton(master=menu_frame, text="Logout", command=lambda: [menu_frame.destroy(),
                                                                                         self.logout()])
        logout_button.pack(pady=12, padx=10)

    def show_leaderboard(self):
        leaderboard_frame = ctk.CTkFrame(master=self.root)
        leaderboard_frame.pack(pady=20, padx=60, fill="both", expand=True)
        leaderboard = game_fuc.get_leaderboard(self.users)
        for r in range(len(leaderboard)):
            for c in range(len(leaderboard[0])):
                leaderboard_entry = ctk.CTkEntry(master=leaderboard_frame, width=200, font=("Arial", 16, "bold"))
                leaderboard_entry.grid(row=r, column=c)
                leaderboard_entry.insert(-1, leaderboard[r][c])
                leaderboard_entry.configure(state="disable")
        back_button = ctk.CTkButton(master=self.root, text="<---", command=lambda: [leaderboard_frame.destroy(),
                                                                                    back_button.forget(),
                                                                                    self.menu()])
        back_button.pack(pady=12, padx=10)

    def start_game(self):
        start_game_frame = ctk.CTkFrame(master=self.root)
        start_game_frame.pack(pady=20, padx=60, fill="both", expand=True)
        start_game_label = ctk.CTkLabel(master=start_game_frame, text="Who are you playing against?")
        start_game_label.pack(pady=12, padx=10)
        start_game_username_entry = ctk.CTkEntry(master=start_game_frame, placeholder_text="Username of the player")
        start_game_username_entry.pack(pady=12, padx=10)
        new_game_button = ctk.CTkButton(master=start_game_frame, text="New Game",
                                        command=lambda: self.new_game(start_game_username_entry.get(),
                                                                      start_game_frame))
        new_game_button.pack(pady=12, padx=10)

    def logout(self):
        self.active_user = None
        self.home()

    def new_game(self, player2, frame):
        if type(game_fuc.new_game(player2, self.users)) is str:
            label = ctk.CTkLabel(master=frame, text=game_fuc.new_game(player2, self.users))
            label.pack(pady=12, padx=10)
            return
        else:
            playing_grid = game_fuc.new_game(player2, self.users)
            frame.destroy()
            game_frame = ctk.CTkFrame(master=self.root)
            game_frame.pack(pady=20, padx=60, fill="both", expand=True)
            self.update_grid(playing_grid, game_frame, self.active_user.get_username(), player2)

    def update_grid(self, playing_grid, game_frame, players_turn: any, player2):
        win_condition = False
        player_label = ctk.CTkLabel(master=self.root, text=players_turn + "'s turn to play(Red pieces).")
        player_label.pack(pady=12, padx=10)
        for r in range(len(playing_grid) + 1):
            for c in range(len(playing_grid[0])):
                if r <= 5:
                    playing_grid_entry = ctk.CTkEntry(master=game_frame, width=40)
                    playing_grid_entry.grid(row=r, column=c)
                    playing_grid_entry.insert(-1, playing_grid[r][c])
                    playing_grid_entry.configure(state="disable")
                else:
                    playing_grid_entry = ctk.CTkEntry(master=game_frame, width=40)
                    playing_grid_entry.grid(row=r, column=c)
                    playing_grid_entry.insert(-1, ctk.CTkButton(master=playing_grid_entry, text="↑",
                                                                command=lambda: self.place_piece(players_turn,
                                                                                                 playing_grid,
                                                                                                 win_condition,
                                                                                                 player2)))

    def place_piece(self, active_player, grid, win_condition, player2):
        pass
