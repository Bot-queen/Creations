import string
import random
import time

pass_list = [
"", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", "",
"", "", "", "", "", "", "", "", "", ""
]

def pass_guesser():
    a = input("Enter password: ")
    while True:
        e = 0
        for j in range(0, 30):
            pass_list[j] = ""
        while e <= 29:
            for i in range(0, 2):
                d = string.ascii_letters[random.randint(0, 51)]
                pass_list[e] = pass_list[e] + d
                if len(pass_list[e]) > 2:
                    break
            if pass_list[e] == a:
                print("Password found! Your pass is", pass_list[e])
            e += 1

pass_guesser()
