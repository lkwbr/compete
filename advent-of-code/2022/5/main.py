from functools import reduce
import re

def part_1():
    with open('input.txt') as f:
        lines = f.readlines()
        i = 0
        data = []
        while True:
            line = lines[i] 
            i += 1
            if not line.strip():
                break
            if '[' not in line:
                # print('xxx', line)
                continue

            # read containers as rows
            chunk_size = 4
            data.append([
                line[i:i+chunk_size].strip()
                for i
                in range(0, len(line), chunk_size)
            ])

        # create stacks for columns (stacks of containers)
        stacks = [[] for s in range(len(data[-1]))]
        for row in reversed(data):
            for i, column_val in enumerate(row):
                if not column_val:
                    continue
                stacks[i].append(column_val)

        # [print(stack) for stack in stacks]

        # read and execute instructions
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if not line:
                continue
            try:
                count, source_stack_num, dest_stack_num = map(int, re.findall(r'\d+', line))
                source_stack = stacks[source_stack_num - 1]
                dest_stack = stacks[dest_stack_num - 1]
            except:
                continue

            # cratemover 9001!
            for _ in range(count):
                dest_stack.append(source_stack.pop())

        # get top values of stack
        top_vals = ''
        for column in stacks:
            top_vals += column[-1].replace(']', '').replace('[', '')
    return top_vals


def part_2():
    with open('input.txt') as f:
        lines = f.readlines()
        i = 0
        data = []
        while True:
            line = lines[i] 
            i += 1
            if not line.strip():
                break
            if '[' not in line:
                # print('xxx', line)
                continue

            # read containers as rows
            chunk_size = 4
            data.append([
                line[i:i+chunk_size].strip()
                for i
                in range(0, len(line), chunk_size)
            ])


        # create stacks for columns (stacks of containers)
        stacks = [[] for s in range(len(data[-1]))]
        for row in reversed(data):
            for i, column_val in enumerate(row):
                if not column_val:
                    continue
                stacks[i].append(column_val)

        # [print(stack) for stack in stacks]
        # exit()

        # read and execute instructions
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if not line:
                continue
            try:
                count, source_stack_num, dest_stack_num = map(int, re.findall(r'\d+', line))
                source_stack = stacks[source_stack_num - 1]
                dest_stack = stacks[dest_stack_num - 1]
            except:
                continue
            # cratemover 9001!
            crate_load = source_stack[-count:]  
            dest_stack += crate_load
            [source_stack.pop() for _ in range(count)]
            print(count, source_stack_num, dest_stack_num)
            [print(stack) for stack in stacks]
            # input()
        # get top values of stack
        top_vals = ''
        for column in stacks:
            top_vals += column[-1].replace(']', '').replace('[', '')
    return top_vals


if __name__ == '__main__':
    x = part_2()
    print('x =', x)