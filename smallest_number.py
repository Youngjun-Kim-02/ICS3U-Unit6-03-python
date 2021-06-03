#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: June 2021
# This program uses a list as a parameter

import random


def find_smallest_number(random_numbers):

    Smallest_number = random_numbers[0]

    for counter in random_numbers:
        if Smallest_number > counter:
            Smallest_number = counter

    return Smallest_number


def main():
    # this function uses a list

    random_numbers = []

    # input
    for loop_counter in range(1, 11):
        a_number = random.randint(1, 100)
        random_numbers.append(a_number)
        print("The random number {0} is: {1} ".format(loop_counter, a_number))
    print("")

    # call the function
    Smallest_number = find_smallest_number(random_numbers)

    # output
    print("The smallest number is: {0} ".format(Smallest_number))


if __name__ == "__main__":
    main()
