import csv
filepath="C:/Users/angel/Desktop/output.csv"
try:
    with open(filepath,"r") as file:
        content=csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found!") 
except PermissionError:
    print("You do not have permission to read this file!")          