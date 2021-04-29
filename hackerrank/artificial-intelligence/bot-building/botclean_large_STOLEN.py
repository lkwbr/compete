#!/usr/bin/env python

from random import shuffle

# Head ends here
def mapping_dirties(posr, posc,board,dim1,dim2):
    '''Build list of dirty cells, along with a matrix of manhattan distances
    between each dirty cell (and the current cell, at first column).
    '''
    dirties=list()
    dirties.append([posr,posc]) # first dirty position is current position
    for i in range(0,dim1):
        for j in range(0,dim2):
            if(board[i][j]=='d'):
                dirties.append([i,j])

    # Get manhattan distance between each cell and all cells behind it (including occupied cell)
    # TODO: Replace with numpy matrix
    mat = [[abs(dirties[x][0]-dirties[y+1][0])+abs(dirties[x][1]-dirties[y+1][1]) for x in range(y+1)] for y in range(len(dirties)-1)]
    return mat, dirties

# TODO: Understand this function
# The hunch is that this is doing the naive approach of travelling salesman where it's finding all permutations of the path and returning the one with the lowest cost
def search(path,costs):
    ''''''
    # NOTE: costs = mat
    loop = 0
    improvement = True
    n=len(path)
    while improvement and loop<n*n:
        improvement = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                loop = loop+1
                if j == n-1:
                    actualPathCost = getCostBetweenCities(costs,path[i-1], path[i])
                    newPathCost = getCostBetweenCities(costs,path[i-1], path[j])
                else:
                    actualPathCost = getCostBetweenCities(costs,path[i-1], path[i]) + getCostBetweenCities(costs,path[j], path[j+1])
                    newPathCost = getCostBetweenCities(costs,path[i-1], path[j]) + getCostBetweenCities(costs,path[i], path[j+1])
                if actualPathCost>newPathCost:
                    temp = path[i]
                    path[i] = path[j]
                    path[j] = temp
                    improvement = True
    return path

def getCostBetweenCities(costs, point1, point2):
    '''Use cost matrix to get cost between two points.'''
    if point1 < point2:
        return costs[point2-2][point1-1]
    else:
        return costs[point1-2][point2-1]

def getTotalCost(costs, path):
    cost = 0
    for i in range(0, len(path)-1):
        j = i+1
        cost += getCostBetweenCities(costs,path[i], path[j])
    return cost

def next_step(oldposr,oldposc,newposr,newposc):
    aux1=oldposr-newposr
    aux2=oldposc-newposc
    if(aux1!=0):
        if(aux1<0):
            print("DOWN")
        else:
            print("UP")
    else:
        if(aux2<0):
            print("RIGHT")
        else:
            print("LEFT")

def test_move(posr, posc, board,dim1,dim2):
    '''Determine cost of being in this position (posc, posr).'''
    mat, dirties = mapping_dirties(posr, posc,board,dim1,dim2)
    print(mat)
    print(dirties)
    path = [y + 1 for y in range(1, len(dirties))] # [2, 3, 4, ..., n - 1]
    solutions = list()
    # Shuffle each path and ???
    for i in range(0,dim1*dim2*4): # ???
        solutions.append(path)
        shuffle(solutions[i])
        solutions[i]=[1]+solutions[i] # make sure path starts at 1 for all?
        solutions[i]=search(solutions[i],mat) # ??
    # Find best solution in all the generated solutions
    bestsolution=solutions[0]
    bestcost=getTotalCost(mat, solutions[0])
    for i in range(1,dim1*dim2*4):
        custo=getTotalCost(mat, solutions[i]) # ??
        if(custo<bestcost):
            bestsolution=solutions[0]
            bestcost=custo
    return bestcost

def next_move(posr, posc, dim1, dim2, board):

    if board[posr][posc] == 'd':
        #print("CLEAN")
        #board[posr][posc]='b'
        return (posr, posc, True)
    else:
        # Determine optimal place to be in immediate 8 surrounding cells:
        #   - Check best y movement, then best x movement
        bestcost=9999
        i=posr
        j=posc

        # Look up
        if(posr-1>=0):
            cost=test_move(posr-1,posc,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                move=1
                i=posr-1
                j=posc

            # TODO: Remove
            return

        if(posr+1<dim1):
            cost=test_move(posr+1,posc,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                i=posr+1
                j=posc

        if(posc-1>=0):
            cost=test_move(posr,posc-1,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                j=posc-1
                i=posr

        if(posc+1<dim2):
            cost=test_move(posr,posc+1,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                j=posc+1
                i=posr

        print('pos = {}, cost = {}'.format((j, i), bestcost))
        print()
        return (i, j, False) 
        
def finish(pos, dims, board):
    '''Return next best dirt cell.'''
    pos += [False]
    while not pos[2]:
        pos = next_move(pos[0], pos[1], dims[0], dims[1], board)
    return pos[:2]

if __name__ == '__main__':
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)