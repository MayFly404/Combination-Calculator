from termcolor import colored, cprint
import os

os.system("cls")

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def nonRepeating():
    n = input("Number of Items: ")
    r = input("Numbers of Items Being Chosen: ")

    numerator = fact(int(n))
    denominator = fact(int(n) - int(r)) * fact(int(r))

    output = numerator/denominator

    cprint(output, "blue")

def repeating():
    n = input("Number of Items: ")
    r = input("Numbers of Items Being Chosen: ")

    output = int(n) ** int(r)

    cprint(output, "blue")

cprint("1. Repeating", "red")
cprint("2. Non-Repeating", "yellow")
choice = input(">> ")

if choice == "1":
    repeating()
elif choice == "2":
    nonRepeating()
else:
    quit()

input("Press Enter to Continue...")
