import os
import pandas as pd

path = "./starwars_project/json_files/"

list_files = os.listdir(path)
starwars_preferences = pd.read_json(path + list_files[0])
for file in list_files[1:]:
 print(file)
 df = pd.read_json(path + file)
 starwars_preferences.loc[len(starwars_preferences)] = df.values.tolist()[0]
print(starwars_preferences.head())
starwars_preferences.to_csv("new.csv")
