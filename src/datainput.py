import pandas as pd
from urllib.request import urlopen
import json


class DataGrabber:
    # URL
    main_path = "http://ddragon.leagueoflegends.com/cdn/13.16.1/data/en_US/champion.json"
    specific_champion_data = "http://ddragon.leagueoflegends.com/cdn/13.16.1/data/en_US/champion/"
    champion_square = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/champion/"

    def get_main_data(self):
        response = urlopen(self.main_path)
        return json.loads(response.read())["data"]

    def get_champion_list(self):
        return pd.DataFrame(self.get_main_data()).columns.tolist()

    def get_champion_img(self, name):
        temp_path = self.champion_square + name + ".png"
        image_temp = urlopen(temp_path)
        raw_img = image_temp.read()
        image_temp.close()
        return raw_img

    def get_champion_data(self, name):
        temp_path = self.specific_champion_data + name + ".json"
        response = urlopen(temp_path)
        json_response = json.loads(response.read())["data"]
        df = pd.DataFrame([(z, h) for i in json_response.values()
                           for z, h in i.items()], columns=['index', 'value'])
        return df.iloc[[2, 3, 6, 8, 9]]

