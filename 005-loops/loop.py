#!/bin/python3


if __name__ == '__main__':
    n = int(input())

    # Print first 10 multiples
    for num in range(1, 11):
        # Using new f string syntax introduced in python 3.6
        print(f"{n} x {num} = {n * num}")