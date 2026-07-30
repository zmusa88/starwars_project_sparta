# main
import json
import os

import character
import homeworld
import film
import species


path = "./json_files/"

list_files = os.listdir(path)

char_data = []

for file_store in list_files:
    with open(os.path.join(path, file_store), 'r') as file:
        #headers = file.readline()
        for line in file:
            values = line.strip().split(",")
            print(values)
            char = character.Character(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11], values[12], values[13], values[14], values[15], values[16], values[17], values[18], values[19], values[20], values[21], values[22], values[23], values[24], values[25], values[26], values[27],values[28], values[29], values[30], values[31])

            char_data.append(char)

#print(headers)
print(char_data)
for c in char_data:
    print(c)


