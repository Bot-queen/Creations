import string
import random
import time

pass_list = [
"", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", ""
]

def pass_guesser():
    while True:
        e = 0
        while e <= 29:
            for i in range(0, 2):
                d = string.ascii_letters[random.randint(0, 51)] + string.digits[random.randint(0, 9)] + string.punctuation[random.randint(0, 31)]
                pass_list[e] = pass_list[e] + d
            time.sleep(2)
            print(pass_list[e])
            e += 1

pass_guesser()
