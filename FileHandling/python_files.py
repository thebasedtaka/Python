
try:
    with open ("sample/newFile.txt", "w") as file:
        file.writelines(["\nDoes this work?", "\nNah this doesn't work"])
except FileNotFoundError as e:
    print ("ERROR", e)
