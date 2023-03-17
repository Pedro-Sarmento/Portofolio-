import customtkinter as ctk

import controllers.gamefunctions as game_fuc
import controllers.userfunctions as user_fuc


class App:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.root = ctk.CTk()
        self.root.geometry("750x400")
        self.users = []
        self.active_user = None
        self.home()
        self.root.resizable(False, False)
        self.root.mainloop()

    def home(self):
        home_frame = ctk.CTkFrame(master=self.root)
        home_frame.pack(pady=20, padx=60, fill="both", expand=True)

        login_button = ctk.CTkButton(master=home_frame, text="Login",
                                     command=lambda: [self.login_interface(), home_frame.destroy()])
        login_button.pack(pady=12, padx=10)
        login_button.place(x=245, y=110)

        register_button = ctk.CTkButton(master=home_frame, text="Register",
                                        command=lambda: [self.register_interface(), home_frame.destroy()])
        register_button.pack(pady=12, padx=10)
        register_button.place(x=245, y=160)

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
            user_fuc.save_object(self.users)

    def menu(self):
        menu_frame = ctk.CTkFrame(master=self.root)
        menu_frame.pack(pady=20, padx=60, fill="both", expand=True)

        start_game_button = ctk.CTkButton(master=menu_frame, text="New Game", command=lambda: [menu_frame.destroy(),
                                                                                               self.start_game()])
        start_game_button.pack(pady=12, padx=10)
        start_game_button.place(x=245, y=110)
        leaderboards_button = ctk.CTkButton(master=menu_frame, text="Leaderboard",
                                            command=lambda: [menu_frame.destroy(),
                                                             self.show_leaderboard()])
        leaderboards_button.pack(pady=12, padx=10)
        leaderboards_button.place(x=245, y=160)

        logout_button = ctk.CTkButton(master=menu_frame, text="Logout", command=lambda: [menu_frame.destroy(),
                                                                                         self.logout()])
        logout_button.pack(pady=12, padx=10)
        logout_button.place(x=245, y=210)

    def show_leaderboard(self):
        leaderboard_frame = ctk.CTkFrame(master=self.root)
        leaderboard_frame.pack(pady=20, padx=60, fill="both", expand=True)
        leaderboard = game_fuc.get_leaderboard(self.users)
        for r in range(len(leaderboard) + 1):
            for c in range(len(leaderboard[0])):
                if r == 0:
                    leaderboard_entry = ctk.CTkEntry(master=leaderboard_frame, width=200, font=("Arial", 16, "bold"))
                    if c == 0:
                        leaderboard_entry.grid(row=r, column=c)
                        leaderboard_entry.insert(-1, "Username")
                    elif c == 1:
                        leaderboard_entry.grid(row=r, column=c)
                        leaderboard_entry.insert(-1, "Games Played")
                    elif c == 2:
                        leaderboard_entry.grid(row=r, column=c)
                        leaderboard_entry.insert(-1, "Wins")
                    leaderboard_entry.configure(state="disable")
                else:
                    leaderboard_entry = ctk.CTkEntry(master=leaderboard_frame, width=200, font=("Arial", 16, "bold"))
                    leaderboard_entry.grid(row=r, column=c)
                    leaderboard_entry.insert(-1, leaderboard[r - 1][c])
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
        start_game_username_entry.place(x=245, y=110)

        new_game_button = ctk.CTkButton(master=start_game_frame, text="New Game",
                                        command=lambda: self.new_game(start_game_username_entry.get(),
                                                                      start_game_frame))
        new_game_button.pack(pady=12, padx=10)
        new_game_button.place(x=245, y=110)

    def logout(self):
        self.active_user = None
        self.home()
        user_fuc.save_object(self.users)



    def new_game(self, player2, frame):
        if type(game_fuc.new_game(player2, self.users)) is str:
            label = ctk.CTkLabel(master=frame, text=game_fuc.new_game(player2, self.users))
            label.pack(pady=12, padx=10)
            return
        else:
            playing_grid = game_fuc.new_game(player2, self.users)
            frame.destroy()
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
            win_condition = False
            self.update_grid(playing_grid, self.active_user.get_username(), player2, win_condition)

    def update_grid(self, playing_grid, players_turn: any, player2, win_condition):
        game_frame = ctk.CTkFrame(master=self.root)
        game_frame.grid()
        game_frame.grid_rowconfigure(0, weight=1)
        game_frame.grid_columnconfigure(0, weight=1)
        button_id = 0

        for r in range(1, len(playing_grid) + 2):
            for c in range(len(playing_grid[0])):
                if r <= 6:

                    actual_row = r - 1
                    actual_column = c
                    if playing_grid[actual_row][actual_column] == 1:
                        playing_grid_entry = ctk.CTkEntry(master=game_frame, width=40, bg_color="red")

                    elif playing_grid[actual_row][actual_column] == 2:
                        playing_grid_entry = ctk.CTkEntry(master=game_frame, width=40, bg_color="blue", fg_color="blue",
                                                           )

                    else:
                        playing_grid_entry = ctk.CTkEntry(master=game_frame, width=40)

                    playing_grid_entry.grid(row=r, column=c, sticky="nwe")
                    playing_grid_entry.insert(-1, playing_grid[actual_row][actual_column])
                    playing_grid_entry.rowconfigure(0, weight=1)
                    playing_grid_entry.columnconfigure(0, weight=1)
                    playing_grid_entry.configure(state="disable")

                else:
                    button = ctk.CTkButton(master=game_frame, text="Place", width=40,
                                           command=lambda column=button_id: [player_entry.destroy(),
                                                                             self.place_piece(players_turn,
                                                                                              playing_grid,
                                                                                              self.active_user.get_username(),
                                                                                              player2,
                                                                                              game_frame,
                                                                                              column)
                                                                             ])
                    button.grid(row=r, column=c, sticky="nwe")
                    button.columnconfigure(0, weight=1)
                    button.rowconfigure(0, weight=1)
                    button_id += 1
        if win_condition is False:
            player_entry = ctk.CTkEntry(master=self.root, width=240)
            player_entry.grid(row=1, column=0)
            player_entry.insert(-1, players_turn + "'s turn to play.")
            player_entry.configure(state="disable")
            player_entry.rowconfigure(0, weight=1)
            player_entry.columnconfigure(0, weight=1)
        else:
            game_frame.destroy()

            win_entry = ctk.CTkEntry(master=self.root, width=240)
            win_entry.grid(row=0, column=0)
            win_entry.insert(-1, players_turn + "is the winner.")
            win_entry.configure(state="disable")
            win_entry.rowconfigure(0, weight=1)
            win_entry.columnconfigure(0, weight=1)

            for i in self.users:
                if i.get_username() == player2:
                    i.add_game_played()
                    self.active_user.add_game_played()
                if i.get_username() == players_turn:
                    i.add_win()

            home_button = ctk.CTkButton(master=self.root, width=60, text="Home", command=lambda: [win_entry.destroy(),
                                                                                                  home_button.destroy(),
                                                                                                  self.menu()])
            home_button.grid(row=1, column=0)
            home_button.columnconfigure(0, weight=1)
            home_button.rowconfigure(1, weight=1)

    def place_piece(self, players_turn, grid, player1, player2, frame, column_id):
        if players_turn == player1:
            grid, win_condition = game_fuc.insert_piece1(grid, column_id)
            frame.destroy()
            if win_condition is True:
                return self.update_grid(grid, players_turn, player2, win_condition)
            return self.update_grid(grid, player2, player2, win_condition)

        else:
            grid, win_condition = game_fuc.insert_piece2(grid, column_id)
            frame.destroy()
            if win_condition is True:
                return self.update_grid(grid, players_turn, player2, win_condition)
            return self.update_grid(grid, player1, player2, win_condition)
