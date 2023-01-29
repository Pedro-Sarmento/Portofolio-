import customtkinter as ctk
import controllers.gamefunctions as game_fuc
import controllers.userfunctions as user_fuc

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()


class App:
    def __init__(self):
        self.root = root
        self.root.geometry("500x400")
        self.login_button = ctk.CTkButton(master=self.root, text="Login",
                                          command=lambda: [self.login_interface(), self.login_button.forget(),
                                                           self.register_button.forget()])
        self.login_button.pack(pady=12, padx=10)
        self.register_button = ctk.CTkButton(master=self.root, text="Register",
                                             command=lambda: [self.register_interface(), self.register_button.forget(),
                                                              self.login_button.forget()])
        self.register_button.pack(pady=12, padx=10)
        self.users = []
        self.active_user = None
        self.root.mainloop()

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
        cancel_button = ctk.CTkButton(master=login_frame, text="Cancel", command=lambda: [login_frame.destroy(), App()])
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
                                      command=lambda: [register_frame.destroy(), App()])
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
            self.active_user = new_user
            self.menu()

    def menu(self):
        start_game_button = ctk.CTkButton(master=root, text="New Game", command=lambda: [self.start_game(),
                                                                                         start_game_button.forget(),
                                                                                         leaderboards_button.forget()])
        start_game_button.pack(pady=12, padx=10)
        leaderboards_button = ctk.CTkButton(master=root, text="Leaderboard", command=lambda: [self.show_leaderboard(),
                                                                                              start_game_button.forget(),
                                                                                              leaderboards_button.forget()])
        leaderboards_button.pack(pady=12, padx=10)

    def show_leaderboard(self):
        pass

    def start_game(self):
        pass
