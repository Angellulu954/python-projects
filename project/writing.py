import json
import csv
txt="I Like Pizza"
filepath="C:/Users/angel/Desktop/output.txt"
try:
    with open(filepath,"w") as file:
        file.write(txt)
        print(f"txt file {filepath} was created.")
except FileExistsError:
    print("This file already exists!")      