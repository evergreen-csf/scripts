names_file = open("staff/data/14s/names.txt", "r")

names = names_file.readlines()

import random

random.shuffle(names)

randoms_file = open("staff/data/14s/names_random.txt", "w")

randoms_file.writelines(names)