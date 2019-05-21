# from comparative_1.guess import *

import sys

class game(object):
    outputList = []
    outputList2 = []
    #def __init__(self, game, word, status, guess, letter, score):
    #    self.game = game;
    #    self.word = word;
    #    self.status = status;
    #    self.guess = guess;
    #    self.letter = letter;
    #    self.score = score;
    #    print()

    def __init__(self):
        print()

    def finalPrint(self):
        from comparative_1 import guess
        go = guess()
        self.outputList = go.calling()
        #self.outputList2 = list(filter(None.__ne__, self.outputList))
        #print(self.outputList2)
        for i in self.outputList:
            if i == 'None':
                continue
            else:
                self.outputList2.append(i)

        #print(self.outputList2)

        print("game    word    status    Bad Guesses    Missed Letters    score")
        print("----    ----    ------    -----------    --------------    -----")
        i = 0
        j = 0
        while i < len(self.outputList2):

            print(self.outputList2[i][0], '     ', self.outputList2[i][1], '  ', self.outputList2[i][2], ' ', self.outputList2[i][3], '            ', self.outputList2[i][4],'               ', self.outputList2[i][5])
            i = i+1



