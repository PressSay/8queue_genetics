import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics','width','780')
Config.set('graphics','height','540')
Config.set('graphics','minimum_width','600')
Config.set('graphics','minimum_height','450')

import random

Builder.load_file('main1.kv')
def view(board):
    # print("the number of child:",count)
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

def show(number,crossover):
    global child1,child2,father,mother
    solutions = []
    while len(solutions) < number:
        father = []
        mother = []
        init(father)
        init(mother)
        thich_nghi_father = thich_nghi(father)
        thich_nghi_mother = thich_nghi(mother)
        while thich_nghi_father != 28 and thich_nghi_mother != 28:
            # count  = count +1
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
    return solutions

class MyLayout(Widget):
    def soundPlayer(self):
        sound = SoundLoader.load('sound/press.mp3')
        if sound:
            sound.play()
    def run(self):
        pass
    def btn(self):
        self.soundPlayer()
        # crossover = random.randint(0,7)
        # solutions = show(1,crossover)
        # for i in range(len(solutions)):
        #     view(solutions[i])
        # the_last=solutions[len(solutions)-1]
        # print(the_last)
    def btn2(self):
        self.soundPlayer()
class MyApp(App):
    def build(self):
        return MyLayout()
    def on_start(self):
        board = self.root.ids.chess_board
        # btn = self.root.btn()
        crossover = random.randint(0,7)
        solutions = show(1,crossover)
        for i in range(len(solutions)):
            view(solutions[i])
        main_board=solutions[len(solutions)-1]
        print(main_board)
        for i in range(8):
            print(main_board[i])
        # photo = Image(file = r"queen_yellow.png")
        for i in range(8):
            board_row = BoxLayout(orientation="horizontal")
            for j in range(1,9):
                if j==main_board[i]: 
                    board_row.add_widget(Button(background_normal="queen_bgden.png",background_color=self.get_color(i,j)))#,text="0",color=[255,167,275,1]))
                    
                else:
                    board_row.add_widget(Button(
                    background_color=self.get_color(i,j),background_normal=""))
            board.add_widget(board_row)
    def get_color(self,i,j):
        is_light_square = (i+j)%2 !=0
        if is_light_square:
            return[1, 0, 0, 1]
        else:
            return[1, 1, 1, 1]
    
if __name__=="__main__":
    MyApp().run()