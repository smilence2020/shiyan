import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down','Right', 'Restart', 'Exit' ]

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions *2))

#print(actions_dict)

def inin():
    
    return 'Game'

def not_game(state):
    responses = defaultdict(lambda:state)
    responses['Restart'],responses['Exit'] = 'Init','Exit'
    return responses[action]

def game():

    if action == 'Restart':
        return 'Init'
    if action == 'Exit':
        return 'Exit'
    if 

state_actions = {
    'Init':init,
    'Win': lambda: not_game('Win')
    'Gameover': lambda: not_game('Gameover')
    'Game':game 
}

def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

class GameField(object):
    def __init__(self, height=4, width =4,win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        selt.reset()

def spawn(self):
    new_element = 4 if randrange(100)>89 else 2
    (i,j)= choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])        

def reset(self):
    if self.score > self.highscore:
        self.hignscore = selt.score
    self.score = 0
    self.field = [[0 for i in range(self.width) for j in range(self.height)]]
    self.spawn()
    self.spawn()


state = 'Init'

while state != 'Exit':
    state = state_actions[state]()
