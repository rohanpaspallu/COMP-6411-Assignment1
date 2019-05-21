# from comparative_1.guess import *

import sys

class game(object):
    outputList = []
    outputList2 = []
    outputList3 = []
    finalValue = ()
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
        from guess import guess
        go = guess()
        self.outputList = go.final_list
        #self.outputList2 = list(filter(None.__ne__, self.outputList))
        #print(self.outputList2)
        for i in self.outputList:
            if i == 'None':
                continue
            else:
                self.outputList2.append(i)

        self.outputList3 = list(filter(None.__ne__, self.outputList2))
        self.finalvalue = tuple(self.outputList3)

        #print(self.outputList3)

        print("game    word    status    Bad Guesses    Missed Letters    score")
        print("----    ----    ------    -----------    --------------    -----")
        i = 0
        j = 0
        while i < len(self.finalvalue):

            print(self.finalvalue[i][0], '     ', self.finalvalue[i][1], '  ', self.finalvalue[i][2], ' ', self.finalvalue[i][3], '            ', self.finalvalue[i][4],'               ', self.finalvalue[i][5])
            i = i+1
