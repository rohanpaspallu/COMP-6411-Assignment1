import random
class stringDatabase:
    w_lis = []
    def readfile(self):
        with open('four_letters.txt') as f:
            for x in f:
                self.w_lis.extend(x.split())
            #lines = f.read().split(" ")
        #lines = [word.replace('\n', ' ') for word in lines]
        #print(self.w_lis)
        self.current_word = random.choice(self.w_lis)
        #print(self.current_word)
        return  self.current_word
