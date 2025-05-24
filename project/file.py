import os 
filepath="C:/Users/angel/Desktop/text"
if os.path.exists(filepath):
    print(f"The location '{filepath}' exists")
    
    if os.path.isfile(filepath):
        print("That is a file.")    
    elif os.path.isdir(filepath):
        print("That is a directory.")
else:
    print("That location doesn't exist.")    