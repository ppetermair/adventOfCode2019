#!/usr/bin/env python3

from os import path

with open(path.join(path.dirname(__file__), "input")) as f:

    total_fuel1 = 0
    total_fuel2 = 0

    for line in f:
        mass = int(line.strip())
        fuel = mass // 3 - 2
        total_fuel1 += fuel

        while fuel > 0:
            total_fuel2 += fuel
            fuel = fuel // 3 - 2


    print('total fuel 1: ' + str(total_fuel1))
    print('total fuel 2: ' + str(total_fuel2))