#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    lenght = len(argv)

    if lenght == 2:
        print("{} argument:".format(lenght - 1))
    elif lenght == 1:
        print("{} arguments.".format(lenght - 1))
    else:
        print("{} arguments:".format(lenght - 1))

    for arg in argv:
        if i == 0:
            i += 1
            continue
        print("{}: {}".format(i, arg))
        i += 1
