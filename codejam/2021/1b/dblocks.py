
import json
import random


def main():
    # interactive mode
    """Stack blocks.
    """

    # the number of test cases, the number of towers, the number of blocks in each tower, and the minimum total score you need to reach to pass this test set
    T, N, B, P = [int(x) for x in input().split()]
    steps = N * B

    def eval_tower(t: list) -> int:
        concat = ''.join([str(x) for x in reversed(t)])
        if not concat:
            return 0
        return int(concat)

    # Algorithm time
    for case in range(T):
        state = [[] for _ in range(N)]
        for step in range(steps):
            block = int(input())
        
            if block == -1:
                exit()

            # Basic algo:  place low blocks in breadth in the first phase and high blocks in depth
            # note:  we don't take into account the face value of the block
            depth_prob = step / steps 
            #place_depth = (block >= 8) or random.random() < depth_prob
            place_depth = (block > 4)

            selected_tower = -1
            
            if place_depth:
                # stack on highest, non-full tower 
                # since we're going left to right here, it will just be the left-most non-full tower
                for i in range(len(state)):
                    t = state[i]
                    if len(t) == B:
                        continue
                    else:
                        t.append(block)
                        selected_tower = i
                        break
            else:
                # place breadth
                # stack on lowest tower
                lowest = 0
                for i in range(len(state)):
                    t = state[i]
                    t_lowest = state[lowest]
                    if len(t) < len(t_lowest): 
                        lowest = i
                state[lowest].append(block)
                selected_tower = lowest

            with open('check', 'w+') as f:
                f.write(json.dumps(state, indent=4))
                f.write(json.dumps([T, N, B, P], indent=4))
                f.write(str(len(state)))
        
            total_sum = sum([eval_tower(t) for t in state])

            #selected_tower = random.randint(0, N)
            #selected_tower = random.randint(0, 3)
            print(selected_tower + 1)
            

main()
