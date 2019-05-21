import random

from game import game


class stringDatabase:
    gameObj = game()
    gameEnd = ()
    w_lis = []
    def readfile(self):

        """
        This function reads the file four_letters.txt from the storage and seperates them by converting it to list of elements
        and finally retrieving random values from the list and returning the value to the
        :return: random word as a string
        """

        with open('four_letters.txt') as f:
            for x in f:
                self.w_lis.extend(x.split())
            #lines = f.read().split(" ")
        #lines = [word.replace('\n', ' ') for word in lines]
        #print(self.w_lis)
        self.current_word = random.choice(self.w_lis)
        #print(self.current_word)
        return  self.current_word

