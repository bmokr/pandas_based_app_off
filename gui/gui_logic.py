import customtkinter as ctk
import logic.dataprocess as vm  # view model
from PIL import ImageTk
from CTkTable import *

# import pandas as pd

comm = vm.OperationsClass()


def clear_frame(where):
    for widgets in where.winfo_children():
        widgets.destroy()


class SearchChampions:  # view 1
    root_name = 'frame'

    def __init__(self, root_name):
        self.root_name = root_name

        self.scrollable_frame_main = ctk.CTkScrollableFrame(master=self.root_name, orientation="vertical")
        self.scrollable_frame_main.pack(fill='both', expand=True)

        self.scrollable_frame_champs = ctk.CTkScrollableFrame(master=self.scrollable_frame_main, width=500, height=200,
                                                              label_text="Champions", orientation="vertical")
        self.scrollable_frame_champs.pack(pady=25)

        self.champion_list_button = ctk.CTkButton(master=self.scrollable_frame_main, text="Get List", width=200,
                                                  command=lambda: self.list_champions())
        self.champion_list_button.pack(pady=20)

        self.pick_champion_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.pick_champion_frame.pack(fill='both', expand=True)

        self.champion_entry = ctk.CTkEntry(master=self.pick_champion_frame,
                                           placeholder_text="Get champion info, eg.: Aatrox", width=300)
        self.champion_entry.pack(side=ctk.LEFT, expand=True, padx=140, pady=25)

        self.champ_ent_button = ctk.CTkButton(master=self.pick_champion_frame, text="Check",
                                              command=lambda: self.get_champion_entry())
        self.champ_ent_button.pack(side=ctk.LEFT, expand=True, pady=25)

        self.changeable_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.changeable_frame.pack(fill='both', expand=True)

    def list_champions(self):
        list_text = comm.show_list()
        for entry in list_text:
            label = ctk.CTkLabel(self.scrollable_frame_champs, text=entry, anchor="w", justify="left")
            label.pack()

    def get_champion_entry(self):
        clear_frame(self.changeable_frame)
        champ = self.champion_entry.get()
        champion_info = comm.open_champion_info(champ)

        photo = ImageTk.PhotoImage(data=champion_info[0])
        photo_label = ctk.CTkLabel(master=self.changeable_frame, text='', image=photo)
        photo_label.image = photo
        photo_label.pack(side=ctk.LEFT, expand=True, pady=25)

        df = champion_info[1]

        new_row = []
        df = df[["index", "value"]].copy()

        columns_values = [["Data", "Info"]]

        table = CTkTable(master=self.changeable_frame, values=columns_values, header_color="dodgerblue4",
                         wraplength=450)

        for index, row in df.iterrows():
            for i in range(df.columns.__len__()):
                new_row.append(row[i])
            table.add_row(new_row)
            new_row = []

        table.pack(expand=True, fill='both', padx=20, pady=20)


class ChampionsStatsTable:  # view 2
    root_name = 'frame'

    def __init__(self, root_name):
        self.root_name = root_name
        self.head_value = 3

        self.scrollable_frame_main = ctk.CTkScrollableFrame(master=self.root_name, orientation="vertical")
        self.scrollable_frame_main.pack(fill='both', expand=True)

        self.columns_values = [["index", "Atk", "Def", "Mgc", "Dif", "Tag1", "Tag2", "Partype"]]

        self.table = CTkTable(master=self.scrollable_frame_main, values=self.columns_values, header_color="dodgerblue4",
                              orientation="horizontal")
        self.table.pack(expand=True, fill='both', padx=20, pady=20)

        self.head_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.head_frame.pack(fill='both', expand=True)

        self.head_entry = ctk.CTkEntry(master=self.head_frame,
                                       placeholder_text="How much columns, eg.: 3", width=300)
        self.head_entry.pack(side=ctk.LEFT, expand=True, padx=140, pady=25)

        self.head_button = ctk.CTkButton(master=self.head_frame, text="Head",
                                         command=lambda: self.head())
        self.head_button.pack(side=ctk.LEFT, expand=True, pady=25)

        self.sort_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.sort_frame.pack(fill='both', expand=True)

        self.sort_entry = ctk.CTkEntry(master=self.sort_frame,
                                       placeholder_text="Sort column, eg.: Tag1 True/False(ascend)", width=300)
        self.sort_entry.pack(side=ctk.LEFT, expand=True, padx=140, pady=25)

        self.sort_button = ctk.CTkButton(master=self.sort_frame, text="Sort",
                                         command=lambda: self.sort())
        self.sort_button.pack(side=ctk.LEFT, expand=True, pady=25)

        self.remove_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.remove_frame.pack(fill='both', expand=True)

        self.remove_entry = ctk.CTkEntry(master=self.remove_frame,
                                         placeholder_text="Remove column, eg.: Tag1", width=300)
        self.remove_entry.pack(side=ctk.LEFT, expand=True, padx=140, pady=25)

        self.remove_button = ctk.CTkButton(master=self.remove_frame, text="Remove",
                                           command=lambda: self.remove())
        self.remove_button.pack(side=ctk.LEFT, expand=True, pady=25)

        self.sum_frame = ctk.CTkFrame(master=self.scrollable_frame_main)
        self.sum_frame.pack(fill='both', expand=True)

        self.sum_entry = ctk.CTkEntry(master=self.sum_frame,
                                      placeholder_text="Sum columns to new column, eg.: Tag1 Tag2", width=300)
        self.sum_entry.pack(side=ctk.LEFT, expand=True, padx=140, pady=25)

        self.sum_button = ctk.CTkButton(master=self.sum_frame, text="Sum",
                                        command=lambda: self.sum())
        self.sum_button.pack(side=ctk.LEFT, expand=True, pady=25)

        self.table_function()

    def table_function(self):
        if self.table.rows > 1:
            for i in range(self.table.rows, 1, -1):
                self.table.delete_row(i)
            self.table.update()

        df = comm.return_main_data(self.head_value)

        new_row = []

        c = []
        for col in df.columns:
            if col != 'level_0':
                c.append(col)
        df = df[c].copy()

        for index, row in df.iterrows():
            for i in range(df.columns.__len__()):
                new_row.append(row[i])
            self.table.add_row(new_row)
            self.table.update()
            new_row = []

    def head(self):
        if self.head_entry.get() != "":
            self.head_value = int(self.head_entry.get())
            self.table_function()

    def sort(self):
        if self.sort_entry.get() != "":
            comm.sort_data_frame(self.sort_entry.get())
            self.table_function()

    def remove(self):
        if self.remove_entry.get() != "":
            index = comm.remove_col(self.remove_entry.get())
            self.table.delete_column(index)
            self.table_function()

    def sum(self):
        if self.sum_entry.get() != "":
            values = comm.sum_up_to_new_column(self.sum_entry.get())
            self.table.add_column(values)#, self.sum_entry.get())
            self.table_function()
