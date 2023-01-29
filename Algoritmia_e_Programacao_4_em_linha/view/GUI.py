import customtkinter as ctk
import controllers.gamefunctions as game_fuc
import controllers.userfunctions as user_fuc


def gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    root.geometry("500x300")
    login_button = ctk.CTkButton(master=root, text="Login", command=login_interface(root))
    login_button.pack(pady=12, padx=10)
    root.mainloop()


def login_interface(master):
    login_frame = ctk.CTkFrame(master= master)
    login_frame.pack(pady=20, padx=60, fill="both", expand=True)
    login_label = ctk.CTkLabel(master=login_frame, text="Login System")
    login_label.pack(pady=12, padx=10)
    login_username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username")
    login_username_entry.pack(pady=12, padx=10)
    login_password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
    login_password_entry.pack(pady=12, padx=10)
    login_submit_button = ctk.CTkButton(master=login_frame, text="Login", command=user_fuc.submit_login())
    login_submit_button.pack(pady=12, padx=10)

