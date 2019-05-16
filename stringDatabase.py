class StringDatabase:
    objectGuess = ""
    countGuess = 0
    countLetter  = 0
    final_guess = []
    def guessing(self, cw, gw, s, g):

        if gw == cw:
            print("number of wrong guesses: ",self.countGuess)
            print("this is true, you are a scholar")
            self.final_guess.append(cw)
            self.final_guess.append("success")
            self.final_guess.append(self.countGuess)
            self.final_guess.append(self.countLetter)
            return self.final_guess
            #self.objectGuess.readfile()
            #self.objectGuess.calling(s, g)

        else:
            print("wrong")
            self.countGuess = self.countGuess + 1
            #printing(s.countGuess)
            print("number of wrong guesses: ",self.countGuess)
            #self.objectGuess.readfile()
            self.objectGuess.calling(s, g)

    def tellme(self, z):
        print("the word is: ", z);

    word_2 = ""

    def letters(self, cw, gl, wo, s, g):
        w_len = len(wo)
        x=0
        wo_list = list(wo)
        if gl in cw:
            while x < w_len:
                if cw[x] == gl:
                    #index = cw.index(gl)
                    #print(index)
                    wo_list[x] = gl

                #print(wo_list)
                #wo_list[index] = gl
                #print(wo_list)
                x = x+1
            print("number of wrong letters: ", self.countLetter)
            word_2 = ''.join(wo_list)
            return word_2
        else:
            self.countLetter = self.countLetter+1;
            print("number of wrong letters: ", self.countLetter)
            # self.objectGuess.readfile()
            self.objectGuess.calling(s, g)

    def quitgame(self):
        print()

    def printing(self):
        return self.countLetter, self.countGuess
        #print("number of misses: ", self.countGuess, " , ", self.countLetter)
