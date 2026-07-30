# main
import json
import csv
import os

import character

path = "./json_files/"

list_files = os.listdir(path)

for list_file in list_files:
    with open(path + list_file) as file:
        data = json.load(file)

    with open('output.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    with open('output.csv', 'r', newline='') as f:
        headers = f.readline().strip().split(",")

        char_data = []

        for line in f:
            values = line.strip().split(",")
            char = {}

            for i in range (len(headers)):
                char[headers[i]] = values[i]

            char_data.append(char)






        # for line in f:
        #     values = line.split(",")
        #     char = character.Character(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
        #                                values[8], values[9], values[10], values[11], values[12], values[13], values[14], values[15], values[16],
        #                                values[17], values[18], values[19], values[20], values[21], values[22],
        #                                values[23], values[24], values[25], values[25], values[26],values[27], values[28], values[29], values[30])
        #     char_data.append(char)



print(headers)
for char in char_data:
    print(char)

#Print headers
# for header in headers:
#     print(f"{header:<15}", end="")
# print()

# Print rows
# for char in char_data:
#     for header in headers:
#         print(f"{str(char[header]):<15}", end="")
#     print()


