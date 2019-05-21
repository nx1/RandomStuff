#tic tac toe by normy

from numpy import random


class Board:
    def __init__(self):
        self.cellstate = [0] * 9
        self.win_state = False
        self.o_turn = False

    def printBoard(self):
        row1 = '|{}| |{}| |{}|'.format(self.cellstate[0],self.cellstate[1],self.cellstate[2])
        row2 = '|{}| |{}| |{}|'.format(self.cellstate[3],self.cellstate[4],self.cellstate[5])
        row3 = '|{}| |{}| |{}|'.format(self.cellstate[6],self.cellstate[7],self.cellstate[8])

    def chooseStarter(self):
        print('Rolling to decide who goes first')
        roll = random.random()
        if roll > 0.5:  
            print('o starts')
            self.o_turn = True
        else:
            print('x starts')
            
    def ToggleTurn(self):
        self.o_turn^=True
        

    def CheckWinState(self):
        '''
        '''
        win = False
        if (self.cellstate[0] == self.cellstate[1] == self.cellstate[2]) and not self.cellstate[0] == '':
            print('123 winner!')
            win = True
        if self.cellstate[3] == self.cellstate[4] == self.cellstate[5]:
            print('456 winner!')
            win = True
        if self.cellstate[6] == self.cellstate[7] == self.cellstate[8]:
            print('789 winner!')
            win = True
        if self.cellstate[0] == self.cellstate[3] == self.cellstate[6]:
            print('147 winner!')
            win = True
        if self.cellstate[1] == self.cellstate[4] == self.cellstate[7]:
            print('258 winner!')
            win = True
        if self.cellstate[2] == self.cellstate[5] == self.cellstate[8]:
            print('369 winner!')
            win = True
        if self.cellstate[6] == self.cellstate[4] == self.cellstate[2]:
            print('753 winner!')
            win = True
        if self.cellstate[0] == self.cellstate[4] == self.cellstate[8]:
            print('159 winner!')
            win = True

        return win
    
    def Move():
        pass




myBoard = Board()

myBoard.chooseStarter()

for i in range(10):
    print('Turn:', i)

    winstate = myBoard.CheckWinState()

    if myBoard.CheckWinState() ==True:
        print('Winner Found!')
        break
    myBoard.ToggleTurn()
