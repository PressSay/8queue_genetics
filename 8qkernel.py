
import random
def view(board, index,count):
    print("the number of child:",count)
    for i in range(8):
        x = board[i] - 1
        for j in range(8):
            if j == x:
                print('[Q]', end='')
            else:
                print('[ ]', end='')
        print()
    
    print()

def check(board):
    h = []
    for i in range(len(board)):
        j = i - 1
        h.append(0)
        while j >= 0:
            if board[i] == board[j] or (abs(board[i] - board[j]) == abs(i - j)):
                h[i] += 1
            j -= 1
        j = i + 1
        while j < len(board):
            if board[i] == board[j] or (abs(board[i] - board[j]) == abs(i - j)):
                h[i] += 1
            j += 1
    return h

def thich_nghi(board):
    count = 0
    for i in range(len(board) - 1):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                count += 1
    for i in range(len(board) - 1):
        for j in range(i + 1, len(board)):
            if abs(board[j] - board[i]) == abs(j - i):
                count += 1
    return 28 - count

def selection(board_1, board_2, crossOver):
    new_board = []
    for i in range(crossOver):
        new_board.append(board_1[random.randint(0, 7)])
    for i in range(crossOver, 8):
        new_board.append(board_2[random.randint(0, 7)])
    return new_board

def new_population(count):
    global father, mother, child1, child2, crossover
    crossover = count
    child1 = selection(father, mother, crossover)
    child2 = selection(mother, father, crossover)

def dot_bien(board):
    global crossover, father, mother
    newchange = -1
    while newchange != 0:
        newchange = 0
        temp = board
        h = check(temp)
        index = h.index(max(h))
        maxFitness = thich_nghi(temp)
        for i in range(1, 9):
            temp[index] = i
            if thich_nghi(temp) > maxFitness:
                maxFitness = thich_nghi(temp)
                newchange = i
            temp = board
        if newchange == 0:
            for i in range(len(board) - 1):
                for j in range(i + 1, len(board)):
                    if board[i] == board[j]:
                        board[j] = random.randint(1, 8)
        else:
            board[index] = newchange


def init(board):
    for i in range(8):
            board.append(random.randint(1, 8))
if __name__ == "__main__":
    number = 8
    
    solutions = []
    crossover = random.randint(0,10)
    count = 0
    while len(solutions) < number:
        father = [3,2,7,5,2,4,1,1]
        mother = [2,4,7,4,8,5,2,2]
        # init(father)
        # init(mother)
        thich_nghi_father = thich_nghi(father)
        thich_nghi_mother = thich_nghi(mother)
        while thich_nghi_father != 28 and thich_nghi_mother != 28:
            count  = count +1
            new_population(crossover)
            dot_bien(child1)
            dot_bien(child2)
            thich_nghi_father = thich_nghi(child1)
            thich_nghi_mother = thich_nghi(child2)
            father = child1
            mother = child2
            print(father)
            print(mother)
        if thich_nghi(father) == 28:
            
            if father not in solutions:
                solutions.append(father)
        else:
            
            if mother not in solutions:
                solutions.append(mother)

    print()

    for i in range(len(solutions)):
        print("case",i)
        view(solutions[i], i,count)

    