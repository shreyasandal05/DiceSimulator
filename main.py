# Alternate (complex!!) method for dice simulator
import random

roll_result = {
    1: "[           ]\n"
       "[     0     ]\n"
       "[           ]",
    2: "[           ]\n"
       "[   0   0   ]\n"
       "[           ]",
    3: "[     0     ]\n"
       "[     0     ]\n"
       "[     0     ]",
    4: "[   0   0   ]\n"
       "[           ]\n"
       "[   0   0   ]",
    5: "[   0   0   ]\n"
       "[     0     ]\n"
       "[   0   0   ]",
    6: "[   0   0   ]\n"
       "[   0   0   ]\n"
       "[   0   0   ]"
}


def dice_simulator():
    number = random.randint(1, 6)
    for key, value in roll_result.items():
        if key == number:
            print(value)


choice = ''
roll = False
while True:
    if roll:
        choice = input('Press y to roll again')
        if choice == 'y':
            print("[-----------]")
            dice_simulator()
            print("[-----------]")
        else:
            exit()
    else:
        roll = True
        print('This is a dice simulator')
        print("[-----------]")
        dice_simulator()
        print("[-----------]")
        