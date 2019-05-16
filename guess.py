import random


class Guess:
    current_word = ""
    database = ""
    last_guess = []

    def __init__(self,s,g):
        self.s = s
        self.g = g

    def readfile(self):
        with open('four_letters.txt') as f:
            lines = f.read().split(" ")
        lines = [word.replace('\n', '') for word in lines]
        #print(lines)
        self.current_word = random.choice(lines)
        print(self.current_word)

    word = "----"
    def calling(self, s, g):
        print(self.word)
        command = input("g = guess, t = tell me, l for a letter, and q to quit")
        gequals = "g"
        tequals = "t"
        lequals = "l"
        qequals = "q"
        if command == gequals:
            gw = input()
            guessing = s.guessing(self.current_word, gw, s, g)
            #self.last_guess = self.database.final_guess
            print(guessing)
        elif command == tequals:
            s.tellme(self.current_word)
        elif command == lequals:
            gl = input()
            self.word = s.letters(self.current_word,gl,self.word, s, g)
            #print(self.word)
            if (self.word != self.current_word):
                self.calling(s, g)
            else:
                print("great you are a scholar")
                self.readfile()
                self.word = "----"
                s.countLetter = 0
                s.countGuess = 0
                self.calling(s, g)
                final_letter = (s.word_2, "success", s.countGuess, s.countLetter)
        elif command == qequals:
            s.quitgame()
        else:
            print("enter correct input")
            self.calling(s,g)
