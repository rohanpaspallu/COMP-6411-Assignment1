

from final_assignment.game import Game
from final_assignment.guess import Guess
from final_assignment.stringDatabase import StringDatabase


def main():
    print("** The great guessing game **")
    s = StringDatabase()
    g = Game()
    m = Guess(s, g)
    s.objectGuess = m
    m.database = s
    g.objectString = s
    m.readfile()
    m.calling(s, g)


main()
