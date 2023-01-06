#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv)
    i = 1
    sum_ = 0
    while i < lenght:
        sum_ += int(argv[i])
        i += 1
    print("{}".format(sum_))
