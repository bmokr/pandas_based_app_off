import customtkinter as ctk
import gui_logic as gl

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1020x780")
root.title("API RIOT")
root.iconbitmap("gui/icon.ico")

title_label = ctk.CTkLabel(root, text="API RIOT", font=("Roboto", 24))
title_label.pack(pady=12)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


def view_search_champions():    # view 1
    gl.clear_frame(frame)
    gl.SearchChampions(frame)


def view_data_tables():    # view 2
    gl.clear_frame(frame)
    gl.ChampionsStatsTable(frame)


button_frame = ctk.CTkFrame(master=root)
button_frame.pack(pady=20, padx=60, fill="both", expand=True)

check_button = ctk.CTkButton(master=button_frame, text="Champions Info", width=200,
                             command=lambda: view_search_champions())
check_button.pack(side=ctk.LEFT, expand=True, pady=25)

tables_button = ctk.CTkButton(master=button_frame, text="Champions Statistics", width=200,
                              command=lambda: view_data_tables())
tables_button.pack(side=ctk.LEFT, expand=True, pady=25)

root.mainloop()
