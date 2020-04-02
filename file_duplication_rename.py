import os

path = ""

os.chdir(path)

b = 0

for i in os.listdir():
    with open(i, "r") as read:
        with open("Duplicate{}.txt".format(i), "w") as write:
            for line in read:
                write.write(line)
    
    names = ["Name1.ext", "Name2.ext", "Name3.ext", "Name4.ext", "Name5.ext", "Name6.ext"]
    os.rename(i, names[b])
    b = b + 1
