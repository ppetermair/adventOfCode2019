#!/usr/bin/env python3

from os import path


def main():
    memory = read_input()
    result_part1 = run_program(memory, 12, 2)
    result_part2 = 0

    for noun in range(100):
        for verb in range(100):
            if run_program(read_input(), noun, verb) == 19690720:
                result_part2 = 100 * noun + verb

    print(result_part1)
    print(result_part2)


def run_program(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    position = 0

    while position < len(memory):
        operation = memory[position]
        if operation == 99:
            break
        elif operation == 1:
            operand1 = memory[memory[position + 1]]
            operand2 = memory[memory[position + 2]]
            location = memory[position + 3]
            memory[location] = operand1 + operand2
        elif operation == 2:
            operand1 = memory[memory[position + 1]]
            operand2 = memory[memory[position + 2]]
            location = memory[position + 3]
            memory[location] = operand1 * operand2
        else:
            raise ValueError('Unknown opcode')

        position += 4

    return memory[0]


def read_input():
    with open(path.join(path.dirname(__file__), "input")) as f:
        return list(map(int,(f.readline().strip().split(","))))


if __name__ == "__main__":
    main()


