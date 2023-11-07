import src.datainput as m  # model
import pandas as pd
import random


class OperationsClass:
    dt = m.DataGrabber()

    def __init__(self):
        response_main_data = self.dt.get_main_data()
        df = pd.DataFrame(response_main_data)
        df = df.transpose()
        df = df[['info', 'tags', 'partype']].copy()

        c = []
        for col in df.columns:
            c.append(col)

        df = df.reset_index()

        # print(type(c.__len__()))
        # print(type(df.columns.__len__()))
        new_row = []

        new_df = pd.DataFrame(columns=["index", "Atk", "Def", "Mgc", "Dif", "Tag1", "Tag2", "Partype"],
                              index=list(df.index.values))  # .set_index('index')

        for index, row in df.iterrows():
            for i in range(c.__len__() + 1):  # while df.columns.__len__() => out of range err
                if isinstance(row[i], list):
                    for each in row[i]:
                        new_row.append(each)
                        if row[i].__len__() == 1:
                            new_row.append("-")
                        i -= 1
                elif isinstance(row[i], dict):
                    for v in row[i].values():
                        new_row.append(v)
                        i -= 1
                else:
                    new_row.append(row[i])
            new_df.loc[index] = new_row
            new_row = []

        self.actual_df = new_df

    def return_main_data(self, how_much=0):
        df = self.actual_df

        # print(type(c.__len__()))
        # print(type(df.columns.__len__()))
        if how_much != 0:
            df = df.head(how_much)
        df = df.reset_index()

        return df

    def open_champion_info(self, champion_name):
        photo = self.dt.get_champion_img(champion_name)
        info = self.dt.get_champion_data(champion_name)

        df = info.reset_index()
        df = df[["index", "value"]].copy()

        new_row = []

        new_df = pd.DataFrame(columns=["index", "value"],
                              index=list(df.index.values))  # .set_index('index')

        for index, row in df.iterrows():
            for i in range(df.columns.__len__()):  # while df.columns.__len__() => out of range err
                if isinstance(row[i], list) and row[i]:
                    new_row.append(row[i][random.randint(0, 2)])
                else:
                    new_row.append(row[i])
            new_df.loc[index] = new_row
            new_row = []

        return photo, new_df

    def sum_up_to_new_column(self, columns_to_sum):
        ca = columns_to_sum.split(' ')
        self.actual_df[columns_to_sum] = self.actual_df[ca[0]] + self.actual_df[ca[1]]
        output = self.actual_df[columns_to_sum].tolist()
        output.insert(0, columns_to_sum)
        return output

    def show_list(self):
        return self.dt.get_champion_list()

    def remove_col(self, column_name):
        index = self.actual_df.columns.get_loc(column_name)
        self.actual_df.drop(column_name, axis=1, inplace=True)
        return index

    def sort_data_frame(self, column_name_asc):
        ca = column_name_asc.split(' ')
        if ca[1] == 'True':
            self.actual_df.sort_values(by=[ca[0]], inplace=True)
        else:
            self.actual_df.sort_values(by=[ca[0]], ascending=False, inplace=True)


# m = OperationsClass()
# print(m.remove_col('Atk'))
