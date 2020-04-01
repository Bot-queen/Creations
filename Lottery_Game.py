import time as t
import random as r

def lottery():
    while True:
        i = input("Would you like to roll the dice? (Y/N): ").upper()
        if i == "Y":
            a = r.randint(1, 6)
            t.sleep(0.4)
            print("\n Your number is... ", a)
            if a == 6:
                t.sleep(0.2)
                print("\n Congrats! You won the second prize!!!")
            elif a == 1:
                t.sleep(0.2)
                print("\nCongrats! You won the first prize!!!")
            else:
                t.sleep(0.2)
                print("\n Aw... Better luck next time!")
            b = input("Wanna do it again? (Y/N): ").upper()
            if b == "Y":
                continue
            elif b == "N":
                break
            else:
                print("Assuming, you have quit...")
                break
            if b == "Y":
                continue
            elif b == "N":
                break
        elif b == "N":
            break
        else:
            print("Not valid response!")
            continue
    t.sleep(0.5)    
    print("\n Thanks for playing!")

lottery()
