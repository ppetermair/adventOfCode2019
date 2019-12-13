#!/usr/bin/env python3

from os import path


def main():
    program = readInput()
    position = 0;
    while position < len(program):
        operation = program[position]
        if operation == 99:
            break
        elif operation == 1:
            operand1 = program[program[position+1]]
            operand2 = program[program[position+2]]
            result = operand1 + operand2
            location = program[position+3]
            program[location] = result
        elif operation == 2:
            operand1 = program[program[position + 1]]
            operand2 = program[program[position + 2]]
            location = program[position + 3]
            result = operand1 * operand2
            program[location] = result
        else:
            raise ValueError('Unknown opcode')

        position += 4

    print(program[0])

def readInput():
    with open(path.join(path.dirname(__file__), "input")) as f:
        input = list(map(int,(f.readline().strip().split(","))))
        input[1] = 12
        input[2] = 2
        return input



if __name__ == "__main__":
    main()


