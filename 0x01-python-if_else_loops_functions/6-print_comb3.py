#!/usr/bin/python3
for i range(0, 9):
    for j in range(1 + 1, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
