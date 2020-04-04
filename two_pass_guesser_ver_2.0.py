import string
import time
import random

pass_list = [
"", "", "",
"", "", ""
]

def pass_guesser():
    while True:
        e = 0
        while e <= 5:
            for j in range(0, 52):
                pass_list[e] = ""
                for k in range(0, 2):
                    d = string.ascii_letters[j]
                    f = string.ascii_letters[random.randint(1, 51)]
                    pass_list[e] = f + d
                time.sleep(1)
                print(pass_list[e])
            e += 1

pass_guesser()
