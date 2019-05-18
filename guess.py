

from comparative_1.stringDatabase import stringDatabase
from comparative_1.game import *

class guess:

    a= stringDatabase()
    word = a.readfile()
    init_word = '----'
    guess_word = ''
    guess_letter = ''
    word_list = []
    no =0
    countGuess = 0
    countLetter = 0
    score = 0
    final_list = []
    finalle = []

    def calling(self):
        #self.word = self.a.readfile()
        print(self.word)
        command = input("g = guess, t = tell me, l for a letter, and q to quit : ")
        gequals = "g"
        tequals = "t"
        lequals = "l"
        qequals = "q"
        if command == gequals:
            self.guess_word = input()
            self.final_list.append(self.guessing_word(self.word, self.guess_word))
            print(self.final_list)
            #self.countLetter = 0
            #self.countGuess = 0
            self.calling()
        elif command == tequals:
            self.final_list.append(self.tell_me(self.word))
            print(self.final_list)
            self.calling()
        elif command == lequals:
            self.guess_letter = input()
            self.final_list.append(self.guessing_letter(self.word, self.guess_letter))
            print(self.final_list)
            #self.countLetter = 0
            #self.countGuess = 0
            self.calling()
        elif command == qequals:
            z = 0
            self.finalle = list(filter(None.__ne__, self.final_list))
            return self.finalle
        else:
            print("wrong input, enter again")
            self.calling()

    def guessing_word(self, w, gw):

        if (w == gw):

            print("this is true, you are a scholar")
            self.no = self.no + 1
            self.word_list = [self.no, w, 'success', self.countGuess, self.countLetter]

            self.init_word = '----'
            self.word = self.a.readfile()
            #self.countGuess = 0
            #self.countLetter = 0
            return self.word_list

        else:
            print("wrong")
            self.countGuess = self.countGuess + 1
            self.score = self.score * 0.90

    def guessing_letter(self, w, gl):
        w_len = len(self.init_word)
        x = 0
        wo_list = list(self.init_word)
        if gl in w:
            while x < w_len:
                if w[x] == gl:
                    #index = cw.index(gl)
                    #print(index)
                    wo_list[x] = gl
                #else:
                    #self.countLetter = self.countLetter + 1
                x = x + 1
            self.init_word = ''.join(wo_list)
            print(self.init_word)
            if (self.init_word != w):
                self.calling()
            else:
                print("great you are a scholar")
                self.no = self.no + 1
                self.word_list = [self.no, w, 'success', self.countGuess, self.countLetter]
                self.init_word = '----'
                self.countLetter = 0
                self.countGuess = 0
                #self.score = self.score + 1
                self.word = self.a.readfile()
                return self.word_list

        else:
            self.countLetter = self.countLetter + 1;
            print("number of wrong letters: ", self.countLetter)
            self.calling()

    def tell_me(self,w):
        print("the word is : ", w)
        self.no = self.no + 1
        self.word_list = [self.no, w, 'Gave up', self.countGuess, self.countLetter]
        self.countGuess = 0
        self.countLetter = 0
        self.word = self.a.readfile()
        return  self.word_list


