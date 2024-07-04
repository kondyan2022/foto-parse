import sys


filename = sys.argv[1]

if len(filename) == 0:
    exit()

with open(filename) as file:
    file.readline()
