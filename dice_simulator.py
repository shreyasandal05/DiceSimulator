# Simpler version using while loop.
import random

print("This is a dice simulator")
x = 'y'
while x == 'y':
    number = random.randint(1, 6)
    if number == 1:
        print("[-----------]\n"
              "[           ]\n"
              "[     0     ]\n"
              "[           ]\n"
              "[-----------]\n")
    if number == 2:
        print("[-----------]\n"
              "[           ]\n"
              "[   0   0   ]\n"
              "[           ]\n"
              "[-----------]\n")
    if number == 3:
        print("[-----------]\n"
              "[     0     ]\n"
              "[     0     ]\n"
              "[     0     ]\n"
              "[-----------]\n")
    if number == 4:
        print("[-----------]\n"
              "[   0   0   ]\n"
              "[           ]\n"
              "[   0   0   ]\n"
              "[-----------]\n")
    if number == 5:
        print("[-----------]\n"
              "[   0   0   ]\n"
              "[     0     ]\n"
              "[   0   0   ]\n"
              "[-----------]\n")
    if number == 6:
        print("[-----------]\n"
              "[   0   0   ]\n"
              "[   0   0   ]\n"
              "[   0   0   ]\n"
              "[-----------]\n")
    x = input("Press y to roll again ")
