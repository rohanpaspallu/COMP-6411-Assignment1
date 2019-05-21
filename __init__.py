from comparative_1.guess import guess
from comparative_1.stringDatabase import stringDatabase
from comparative_1.game import game

def main():
    print("** The great guessing game **")

    stringDatabaseObject = stringDatabase()
    guessObject =guess()
    gameObject = game()
    stringDatabaseObject.readfile()
    guessObject.calling()
    gameObject.finalPrint()

main()
